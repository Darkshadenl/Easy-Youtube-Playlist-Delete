# Easy YouTube Playlist Manager

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

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

5. **Run the application**:
   ```bash
   python manage-playlists.py
   ```

## 📋 Requirements
- Python 3.7+
- A YouTube API OAuth2 credentials file (`credentials.json`).
- Modules: `google-auth`, `google-auth-oauthlib`, `google-api-python-client`, `tk`, `Pillow`.

## 📸 Screenshots
<img width="736" alt="app screenshot" src="https://github.com/user-attachments/assets/efc5b2e1-7280-4a53-b56e-1a2bb4b0f8f2" />

## 💡 How to Use
1. Launch the application.
2. Log in with your Google account via OAuth2.
3. Search for playlists, select them, and safely delete them.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

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

4. **Set Up OAuth Consent Screen**  
   Navigate to "OAuth Consent Screen." Choose "External," fill in the required fields, and save.

5. **Create OAuth Credentials**  
   Go to "Credentials" > "Create Credentials" > "OAuth 2.0 Client IDs." Select "Desktop App" and create.

6. **Download `credentials.json`**  
   After creating the credentials, click "Download JSON." Save it as `credentials.json`.

7. **Move File to Project Folder**  
   Place the `credentials.json` file in the root directory of the project.

8. **Test the Application**  
   Run the program to verify the credentials work.

Done! You’re ready to manage your YouTube playlists. 🎉
