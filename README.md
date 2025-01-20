# Windows Temp Folder Cleanup Script

![temp_cleaner](https://github.com/user-attachments/assets/196c1f56-71f3-4e94-997b-47e8ac5ebb6e)

This Python script automates the process of cleaning up the Windows Temp folder, helping free up disk space by deleting unnecessary files and directories. The script targets the `Temp` folder in the current user's local directory (`AppData/Local/Temp`) and removes all files, symbolic links, and subdirectories. It safely handles permission errors, ensuring that files in use or protected by the system are skipped.

### Features:
- Deletes temporary files and folders in the `Temp` directory.
- Safely handles permission errors without interrupting the cleanup process.
- Simple and efficient solution to free up disk space on Windows.

### Requirements:
- Python 3.x
- Permissions to access and modify the `Temp` folder.

### Usage:
Clone the repository and run the script:
```bash
python cleanup_temp.py
```

Osman KAHRAMAN
