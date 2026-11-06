import os

def restore_desktop_files():
    """
    Restore all renamed files on Desktop back to their original names.
    Based on the file properties and the original rename log.
    """
    
    # Define the folder
    folder = r"C:\Users\spoor\OneDrive\Desktop"
    
    # Mapping: current_name -> original_name
    # Based on the rename sequence shown in the console output
    rename_map = {
        "spoorthi_001.pdf": "BIg Data Analytics-Module-2.pptx.pdf",
        "spoorthi_002.pdf": "DISTRIBUTED SYSTEMS NOTES_MODULE1.pdf",
        "spoorthi_003.lnk": "Downloads - Shortcut (2).lnk",
        "spoorthi_004.lnk": "Downloads - Shortcut.lnk",
        "spoorthi_005.exe": "Firefox.exe",
        "spoorthi_006.lnk": "GNU Prolog.lnk",
        "spoorthi_007.pdf": "ISRO.pdf",
        "spoorthi_008.docx": "Internship_Report[1].docx",
        "spoorthi_009.lnk": "MongoDBCompass.lnk",
        "spoorthi_010.docx": "Resume_Example.docx",
        "spoorthi_011.pdf": "Spoorthi J Shetty.pdf",
        "spoorthi_012.pdf": "Spoorthishetty_resume.pdf",
        "spoorthi_013.lnk": "Spyder 6.lnk",
        "spoorthi_014.lnk": "Telegram.lnk",
        "spoorthi_015.lnk": "Visual Studio Code - Copy.lnk",
        "spoorthi_016.pdf": "data assignmen.pdf",
        "spoorthi_017.pdf": "datavisulation.certificate.pdf",
        "spoorthi_018.ini": "desktop.ini",
        "spoorthi_019.zip": "imaginary-ai.zip",
        "spoorthi_020.pdf": "intcerti.pdf",
        "spoorthi_021.jpg": "internship.jpg",
        "spoorthi_022.zip": "scr.zip",
        "spoorthi_023.zip": "script.zip",
        "spoorthi_024.jpg": "sign.jpg",
        "spoorthi_025.pdf": "sjs.007.pdf",
        "spoorthi_026.lnk": "spoorthi - Chrome.lnk",
        "spoorthi_027.pdf": "spoorthi resume.pdf",
        "spoorthi_028.docx": "spoorthi shetty.resume.docx",
        "spoorthi_029.docx": "spoorthishettyresume.docx",
        "spoorthi_030.jpg": "sshot.jpg",
        "spoorthi_031.pdf": "ssss.pdf",
        "spoorthi_032.zip": "visionary-ai-studio.zip"
    }
    
    print("=" * 70)
    print("RESTORE ORIGINAL FILE NAMES")
    print("=" * 70)
    print(f"\nFolder: {folder}")
    print(f"Files to restore: {len(rename_map)}")
    print("\n" + "=" * 70)
    
    # Show what will be restored
    print("\nFiles that will be renamed:")
    print("-" * 70)
    for current, original in rename_map.items():
        print(f"  {current} → {original}")
    
    print("\n" + "=" * 70)
    confirm = input("\nProceed with restoration? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("❌ Restoration cancelled")
        return
    
    print("\n[RESTORING FILES...]\n")
    
    success_count = 0
    not_found = 0
    errors = 0
    
    for current_name, original_name in rename_map.items():
        current_path = os.path.join(folder, current_name)
        original_path = os.path.join(folder, original_name)
        
        try:
            if os.path.exists(current_path):
                # Check if original name already exists (conflict)
                if os.path.exists(original_path):
                    print(f"⚠️  Conflict: {original_name} already exists, skipping")
                    errors += 1
                else:
                    os.rename(current_path, original_path)
                    print(f"✓ {current_name} → {original_name}")
                    success_count += 1
            else:
                print(f"✗ Not found: {current_name}")
                not_found += 1
                
        except Exception as e:
            print(f"✗ Error with {current_name}: {e}")
            errors += 1
    
    print("\n" + "=" * 70)
    print("RESTORATION COMPLETE!")
    print("=" * 70)
    print(f"✅ Successfully restored: {success_count} files")
    if not_found > 0:
        print(f"⚠️  Files not found: {not_found}")
    if errors > 0:
        print(f"❌ Errors: {errors}")
    print("=" * 70)

if __name__ == "__main__":
    restore_desktop_files()