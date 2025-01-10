# Easy YouTube Playlist Manager

![Python](https://img.shields.io/badge/Python-3.x-blue)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## 🛠️ Overview
The **Easy YouTube Playlist Manager** is a desktop application that allows you to easily manage your YouTube playlists. 
With a user-friendly interface, you can search, view, and delete playlists effortlessly. 
All of this is powered by the official YouTube API for seamless integration.

## 🚀 Features
- **Quick Search**: Search through your playlists using a handy search bar.
- **Select and Delete**: Manage multiple playlists at once with a single click.
- **Visual Feedback**: Selections are highlighted for an intuitive experience.
- **Thumbnail Support**: View playlist thumbnails directly in the interface.
- **Secure OAuth2 Authentication**: Your data stays private and secure.

## 📂 File Structure
```
Darkshadenl-Easy-Youtube-Playlist-Delete/
├── LICENSE
├── manage-playlists.py
├── requirements.txt
```

## 🛠️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Darkshadenl/Easy-Youtube-Playlist-Delete.git
   cd Easy-Youtube-Playlist-Delete
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your `credentials.json`**:
   Download your YouTube API OAuth2 client credentials and place the file in the project root.
   **I've added a more complete tutorial at the bottom of this readme!**

4. Use Ngrok to enable communication between your device and the web.

5. **Run the application**:
   ```bash
   python manage-playlists.py
   ```

## 📋 Requirements
- Python 3.7+
- A YouTube API OAuth2 credentials file (`credentials.json`).
- Modules: `google-auth`, `google-auth-oauthlib`, `google-api-python-client`, `tk`, `Pillow`.

## 📸 Screenshots
<img width="1270" alt="app screenshot" src="https://github.com/user-attachments/assets/992bab37-0245-49f9-b44e-695c9e0db876" />


## 💡 How to Use
1. Launch the application.
2. Log in with your Google account via OAuth2.
3. Search for playlists, select them, and safely delete them.

## 📜 License
This project is licensed under the GNU General Public License. See the [LICENSE](LICENSE) file for details.

## ⭐ Contribute
Feel free to open an issue or submit a pull request! 😊

---

With **Easy YouTube Playlist Manager**, managing your YouTube playlists becomes effortless and efficient. Try it today!

---

### 🔑 How to Obtain `credentials.json` for YouTube API

Follow these steps to generate your `credentials.json` file:

1. **Go to Google Cloud Console**  
   Visit [https://console.cloud.google.com/](https://console.cloud.google.com/).

2. **Create a New Project**  
   Click "Create Project," name it, and confirm.

3. **Enable YouTube Data API v3**  
   Go to "APIs & Services" > "Library." Search for **YouTube Data API v3** and enable it.

4. **Set Up YouTube Data API v3**  
   Go through the different screens and fill in the details
   If you use NGrok to enable communication between your app and the outside, register them under the Branding tab.
   Then create a client under 'Clients'.
   If it keeps redirecting you to 'Branding', just start an in private browser tab, log in, and try again. That fixed it for me.

5. **Create OAuth Credentials**  
   Go to "Credentials" > "Create Credentials" > "OAuth 2.0 Client IDs." Select "Desktop App" and create.

7. **Download `credentials.json`**  
   After creating the credentials, click "Download JSON." Save it as `credentials.json`.
   Can be found under 'Clients'. A small download button is visible under 'Client secrets'.

9. **Move File to Project Folder**  
   Place the `credentials.json` file in the root directory of the project.

10. **Test the Application**  
   Run the program to verify the credentials work.

Done! You’re ready to manage your YouTube playlists. 🎉
