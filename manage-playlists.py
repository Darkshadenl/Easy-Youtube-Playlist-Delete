import tkinter as tk
import sys
import requests
from io import BytesIO
from tkinter import messagebox, ttk
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from PIL import Image, ImageTk  # Zorg ervoor dat Pillow geïnstalleerd is

# Scopes definiëren
SCOPES = [
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtubepartner",
    "https://www.googleapis.com/auth/youtube",
]


class YouTubePlaylistManager:
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Playlist Manager")
        self.playlists = []
        self.selected_playlists = set()
        self.playlist_images = {}

        # OAuth2 Authenticatie
        self.service = self.authenticate()

        # GUI Elementen
        self.create_widgets()
        self.fetch_playlists()
        self.active_playlist_window = None

    def authenticate(self):
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        service = build("youtube", "v3", credentials=creds)
        return service

    def create_widgets(self):
        # Zoekbalk
        search_frame = tk.Frame(self.master)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Zoeken: ").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.update_playlist_view)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=50)
        search_entry.pack(side=tk.LEFT)

        # Style configuratie voor de treeview
        style = ttk.Style()
        style.configure(
            "Treeview",
            rowheight=30,  # Grotere rijen voor betere zichtbaarheid
            font=("Arial", 10),
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold"),
            padding=(5, 5),
        )

        # Playlists Treeview met twee kolommen: Titel en Checkbox
        self.tree = ttk.Treeview(
            self.master,
            columns=("Title", "Checkbox"),
            show="headings",
            style="Treeview",
        )

        self.tree.heading("Title", text="Playlist Naam")
        self.tree.heading("Checkbox", text="")

        # Stel de kolom breedtes in
        self.tree.column("Title", width=500, anchor="w")  # Links uitlijnen
        self.tree.column("Checkbox", width=50, anchor="e")  # Rechts uitlijnen

        # Voeg scrollbar toe
        scrollbar = ttk.Scrollbar(
            self.master, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack de elementen
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True, side=tk.LEFT)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        # Bewerk de Treeview items zodat ze de afbeelding bevatten
        self.tree.bind("<Button-1>", self.handle_click)

        # Delete Knop met moderne styling
        delete_button = tk.Button(
            self.master,
            text="Verwijderen",
            command=self.delete_playlists,
            bg="#ff4444",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            font=("Arial", 10, "bold"),
        )
        delete_button.pack(pady=10)

    def handle_click(self, event):
        # Identificeer de regio waar geklikt is
        region = self.tree.identify_region(event.x, event.y)
        if region == "cell":
            # Krijg de kolom en item ID
            column = self.tree.identify_column(event.x)
            item = self.tree.identify_row(event.y)

            if item:
                if column == "#2":  # Checkbox kolom
                    if item in self.selected_playlists:
                        self.selected_playlists.remove(item)
                    else:
                        self.selected_playlists.add(item)
                    self.update_playlist_view()
                elif column == "#1":  # Title kolom
                    self.show_playlist_items(item)

    def fetch_playlists(self):
        request = self.service.playlists().list(
            part="snippet",  # Verwijder contentdetails
            mine=True,
            maxResults=50,
        )
        while request:
            response = request.execute()
            for item in response.get("items", []):
                snippet = item["snippet"]
                thumbnail_url = snippet["thumbnails"].get("default", {}).get("url")

                self.playlists.append(
                    {
                        "id": item["id"],
                        "title": snippet["title"],
                        "thumbnail_url": thumbnail_url,
                    }
                )
                if thumbnail_url:
                    self.load_thumbnail(item["id"], thumbnail_url)

            request = self.service.playlists().list_next(request, response)
        self.update_playlist_view()

    def load_thumbnail(self, playlist_id, url):
        try:
            # Download en verwerk de thumbnail
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            # Resize naar een geschikte grootte voor de UI
            img = img.resize((30, 30), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.playlist_images[playlist_id] = photo
        except Exception as e:
            print(f"Fout bij laden thumbnail voor playlist {playlist_id}: {e}")
            self.playlist_images[playlist_id] = None

    def update_playlist_view(self, *args):
        search_text = self.search_var.get().lower()
        scroll_pos = self.tree.yview()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for playlist in self.playlists:
            if search_text in playlist["title"].lower():
                checkmark = "✅" if playlist["id"] in self.selected_playlists else "⬜"
                # Voeg de thumbnail toe als die beschikbaar is
                image = self.playlist_images.get(playlist["id"])
                self.tree.insert(
                    "",
                    "end",
                    iid=playlist["id"],
                    values=(playlist["title"], checkmark),
                    image=image if image else "",  # Gebruik de thumbnail als die er is
                )

        try:
            self.tree.yview_moveto(scroll_pos[0])
        except:
            pass

    def show_playlist_items(self, playlist_id):
        if self.active_playlist_window and self.active_playlist_window.winfo_exists():
            self.active_playlist_window.destroy()

        # Zoek de playlist titel
        playlist_title = next(
            (p["title"] for p in self.playlists if p["id"] == playlist_id),
            "Onbekende Playlist",
        )

        # Maak een nieuw window
        playlist_window = tk.Toplevel(self.master)
        self.active_playlist_window = playlist_window  # Sla referentie op
        playlist_window.title(f"Items in playlist: {playlist_title}")
        playlist_window.geometry("800x600")

        # Maak een nieuwe treeview voor de playlist items
        columns = ("Titel", "Kanaal", "Datum")
        tree = ttk.Treeview(
            playlist_window, columns=columns, show="headings", style="Treeview"
        )

        # Configureer de kolommen
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="w")

        # Stel kolombreedtes in
        tree.column("Titel", width=400)
        tree.column("Kanaal", width=200)
        tree.column("Datum", width=150)

        # Voeg scrollbar toe
        scrollbar = ttk.Scrollbar(
            playlist_window, orient="vertical", command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack de elementen
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        # Laad de playlist items
        try:
            # Toon laad indicator
            loading_label = tk.Label(
                playlist_window, text="Items laden...", font=("Arial", 12)
            )
            loading_label.pack(pady=20)
            playlist_window.update()

            # Haal playlist items op
            request = self.service.playlistItems().list(
                part="snippet", playlistId=playlist_id, maxResults=50
            )

            while request:
                response = request.execute()
                for item in response.get("items", []):
                    snippet = item["snippet"]
                    published_at = snippet["publishedAt"].split("T")[0]  # Alleen datum
                    tree.insert(
                        "",
                        tk.END,
                        values=(
                            snippet["title"],
                            snippet["videoOwnerChannelTitle"],
                            published_at,
                        ),
                    )
                request = self.service.playlistItems().list_next(request, response)

            # Verwijder laad indicator
            loading_label.destroy()

        except Exception as e:
            messagebox.showerror(
                "Fout", f"Fout bij het ophalen van playlist items: {str(e)}"
            )
            playlist_window.destroy()
            return

        # Voeg een sluit knop toe
        close_button = tk.Button(
            playlist_window,
            text="Sluiten",
            command=playlist_window.destroy,
            bg="#ff4444",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            font=("Arial", 10, "bold"),
        )
        close_button.pack(pady=10)

    def delete_playlists(self):
        if not self.selected_playlists:
            messagebox.showwarning(
                "Geen selectie", "Selecteer ten minste één playlist om te verwijderen."
            )
            return
        confirm = messagebox.askyesno(
            "Bevestigen",
            f"Weet je zeker dat je de geselecteerde {len(self.selected_playlists)} playlists wilt verwijderen?",
        )
        if confirm:
            for playlist_id in list(self.selected_playlists):
                try:
                    self.service.playlists().delete(id=playlist_id).execute()
                    self.playlists = [
                        p for p in self.playlists if p["id"] != playlist_id
                    ]
                    self.tree.delete(playlist_id)
                    self.selected_playlists.remove(playlist_id)
                except Exception as e:
                    messagebox.showerror(
                        "Fout",
                        f"Fout bij het verwijderen van playlist {playlist_id}: {e}",
                    )
            messagebox.showinfo("Succes", "Geselecteerde playlists zijn verwijderd.")

    def on_window_close(self):
        # Optioneel: cleanup wanneer het hoofdvenster sluit
        if self.active_playlist_window and self.active_playlist_window.winfo_exists():
            self.active_playlist_window.destroy()
        self.master.destroy()


def main():
    root = tk.Tk()
    root.geometry("600x400")
    YouTubePlaylistManager(root)
    root.mainloop()


if __name__ == "__main__":
    print("Python versie:", sys.version)
    print("Tkinter versie:", tk.TkVersion)
    main()
