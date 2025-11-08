<h1 align="center">SafePaste</h1>

SafePaste is a simple, secure, cross-platform clipboard/text sharing tool. It allows you to send text from one machine to another by leveraging a Firebase Realtime Database as a temporary backend. All text is encrypted client-side before being sent, and decrypted only upon fetching, ensuring that the data on the server is not readable.

<table>
 <tr>
  <td><img src="https://github.com/user-attachments/assets/83f64fd3-26b0-4225-8fbb-ced8b310ed3d" alt="SafePaste Send Tab" width="400"></td>
  <td><img src="https://github.com/user-attachments/assets/ccb4389b-8e7d-4364-a4eb-a83487d913e5" alt="SafePaste Receive Tab" width="400"></td>
 </tr>
</table>

## Features

  * **Secure:** All data is encrypted locally using `cryptography.fernet` before being uploaded.
  * **Simple UI:** A minimal, tabbed interface for "SEND" and "RECEIVE" actions, built with PyQt6.
  * **Key-Based Access:** Data is fetched using a unique, randomly generated ID combined with its encryption key.
  * **Cross-Platform:** As a Python/PyQt app, it can run on Windows, macOS, and Linux.

## Setup Instructions

### 1\. Prerequisites

You must have Python 3 installed on your system.

### 2\. Install Dependencies

This project requires several Python packages. You can install them all using pip:

```bash
pip install -r requirements.txt
```

### 3\. Firebase Setup (Required)

This application uses **Firebase Realtime Database** to store the encrypted text snippets. You must set up your own Firebase project for the application to work.

1.  **Create a Firebase Project:**

      * Go to the [Firebase Console](https://console.firebase.google.com/).
      * Click "Add project" and follow the on-screen instructions to create a new project.

2.  **Set up Realtime Database:**

      * In your new project's console, go to **Build \> Realtime Database**.
      * Click "Create Database".
      * Select a location (e.g., `us-central1`).
      * Start in **locked mode** (you can edit rules later if needed, but the app uses admin credentials).
      * After the database is created, copy its URL. It will look something like: `https://your-project-name-12345-default-rtdb.firebaseio.com/`.

3.  **Generate a Service Account Key:**

      * In the Firebase console, go to **Project Settings** (click the gear icon ⚙️ next to "Project Overview").
      * Go to the **Service accounts** tab.
      * Click **"Generate new private key"**.
      * A warning will appear; click **"Generate key"** to confirm.
      * A JSON file will be downloaded to your computer.

4.  **Run & Configure the Application:**
    * Run the application from your terminal:
        ```bash
        python3 main.py
        ```
    * On the first run, a **"Configurations"** setup dialog will appear.
    * Provide your **Realtime Database URL** (from step 2) and the **service account JSON file** (from step 3).
    * Click **"OK"** to save and launch the app.

## Usage Instructions

After completing the setup, you can run the application from your terminal:

```bash
python3 main.py
```

### To Send Text

1.  Run the application. You will be on the **SEND** tab by default.
2.  Type or paste the text you wish to share into the text box ("Enter data to send...").
3.  Click the **SEND** button.
4.  The application will encrypt the data, upload it to Firebase, and generate a unique ID and key.
5.  The combined ID (in the format `[key_string] : [random_id]`) will appear in the label below the button (e.g., `ID - gQ...cE= : 4x...E0`).
6.  Click the **Copy** button to copy this full ID string to your clipboard.

### To Receive Text

1.  On the receiving machine, run the application.
2.  Click the **RECEIVE** tab.
3.  Paste the full ID string (e.g., `gQ...cE= : 4x...E0`) that you copied from the sending machine into the "Enter the unique ID\!\!" field.
4.  Click the **FETCH** button.
5.  The application will use the ID to find the data in Firebase and use the key to decrypt it. The original text will appear in the read-only text box.

## License

This project is licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for full details.
