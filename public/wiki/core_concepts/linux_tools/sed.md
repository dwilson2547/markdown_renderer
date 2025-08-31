Here’s a **comprehensive `sed` cheat sheet** with common commands and practical examples:

---

### **`sed` Cheat Sheet**
`sed` (stream editor) is a powerful Linux command for parsing and transforming text.

---

- [**`sed` Cheat Sheet**](#sed-cheat-sheet)
- [**1. Basic Syntax**](#1-basic-syntax)
- [**2. Common Commands**](#2-common-commands)
  - [**2.1. Substitution (`s`)**](#21-substitution-s)
  - [**2.2. Global Substitution (`g`)**](#22-global-substitution-g)
  - [**2.3. Case-Insensitive Substitution (`i`)**](#23-case-insensitive-substitution-i)
  - [**2.4. Delete Lines (`d`)**](#24-delete-lines-d)
  - [**2.5. Print Lines (`p`)**](#25-print-lines-p)
  - [**2.6. Line Numbers**](#26-line-numbers)
  - [**2.7. Insert (`i`) and Append (`a`)**](#27-insert-i-and-append-a)
  - [**2.8. Change Line (`c`)**](#28-change-line-c)
  - [**2.9. In-Place Editing (`-i`)**](#29-in-place-editing--i)
  - [**2.10. Multiple Commands (`-e`)**](#210-multiple-commands--e)
  - [**2.11. Address Ranges**](#211-address-ranges)
  - [**2.12. Regular Expressions**](#212-regular-expressions)
  - [**2.13. Read from a File (`r`)**](#213-read-from-a-file-r)
  - [**2.14. Write to a File (`w`)**](#214-write-to-a-file-w)
  - [**2.15. Quit (`q`)**](#215-quit-q)
- [**3. Advanced Examples**](#3-advanced-examples)
  - [**3.1. Remove Empty Lines**](#31-remove-empty-lines)
  - [**3.2. Remove Comments**](#32-remove-comments)
  - [**3.3. Double Space a File**](#33-double-space-a-file)
  - [**3.4. Number Lines**](#34-number-lines)
  - [**3.5. Extract Email Addresses**](#35-extract-email-addresses)
- [**4. Common Use Cases**](#4-common-use-cases)
- [**5. Tips and Tricks**](#5-tips-and-tricks)


### **1. Basic Syntax**
```bash
sed [options] 'command' [input-file]
```
- **Options**:
  - `-n`: Suppress automatic printing of pattern space.
  - `-i`: Edit files in-place (use with caution!).
  - `-e`: Specify multiple commands.
  - `-f`: Read commands from a file.

---

### **2. Common Commands**

#### **2.1. Substitution (`s`)**
Replace text patterns.
```bash
sed 's/old-text/new-text/' file.txt
```
- Replace the **first occurrence** of `old-text` with `new-text` in each line.

**Example**:
```bash
sed 's/foo/bar/' file.txt
```
- Replaces `foo` with `bar` in `file.txt`.

---

#### **2.2. Global Substitution (`g`)**
Replace **all occurrences** of a pattern in a line.
```bash
sed 's/old-text/new-text/g' file.txt
```
**Example**:
```bash
sed 's/apple/orange/g' file.txt
```
- Replaces all instances of `apple` with `orange`.

---

#### **2.3. Case-Insensitive Substitution (`i`)**
```bash
sed 's/old-text/new-text/gi' file.txt
```
**Example**:
```bash
sed 's/cat/dog/gi' file.txt
```
- Replaces `cat`, `Cat`, `CAT`, etc., with `dog`.

---

#### **2.4. Delete Lines (`d`)**
Delete lines matching a pattern.
```bash
sed '/pattern/d' file.txt
```
**Example**:
```bash
sed '/error/d' logfile.txt
```
- Deletes all lines containing `error`.

---

#### **2.5. Print Lines (`p`)**
Print lines matching a pattern.
```bash
sed -n '/pattern/p' file.txt
```
**Example**:
```bash
sed -n '/success/p' logfile.txt
```
- Prints only lines containing `success`.

---

#### **2.6. Line Numbers**
Print or delete lines by number.
```bash
sed -n '5p' file.txt          # Print line 5
sed '3d' file.txt             # Delete line 3
sed -n '1,10p' file.txt       # Print lines 1 to 10
```
**Example**:
```bash
sed -n '10,20p' data.txt
```
- Prints lines 10 to 20.

---

#### **2.7. Insert (`i`) and Append (`a`)**
Insert or append text before/after a line.
```bash
sed '3i\new line' file.txt    # Insert before line 3
sed '5a\new line' file.txt    # Append after line 5
```
**Example**:
```bash
sed '1i\# Header' file.txt
```
- Inserts `# Header` at the beginning of the file.

---

#### **2.8. Change Line (`c`)**
Replace an entire line.
```bash
sed '3c\new line' file.txt
```
**Example**:
```bash
sed '2c\This is the new second line' file.txt
```
- Replaces the second line with `This is the new second line`.

---

#### **2.9. In-Place Editing (`-i`)**
Edit files directly (use with caution!).
```bash
sed -i 's/old/new/' file.txt
```
**Example**:
```bash
sed -i 's/windows/linux/g' config.txt
```
- Replaces `windows` with `linux` in `config.txt` and saves changes.

---

#### **2.10. Multiple Commands (`-e`)**
Execute multiple commands.
```bash
sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt
```
**Example**:
```bash
sed -e 's/red/blue/' -e 's/small/large/' colors.txt
```
- Replaces `red` with `blue` and `small` with `large`.

---

#### **2.11. Address Ranges**
Apply commands to a range of lines.
```bash
sed '3,6s/old/new/' file.txt
```
**Example**:
```bash
sed '10,20s/yes/no/' survey.txt
```
- Replaces `yes` with `no` in lines 10 to 20.

---

#### **2.12. Regular Expressions**
Use regex for complex pattern matching.
```bash
sed -n '/^[A-Z]/p' file.txt       # Print lines starting with a capital letter
sed 's/[0-9]\{3\}/NUM/g' file.txt # Replace 3-digit numbers with "NUM"
```
**Example**:
```bash
sed -n '/^[A-Za-z]/p' names.txt
```
- Prints lines starting with a letter.

---

#### **2.13. Read from a File (`r`)**
Insert the contents of a file.
```bash
sed '3r newfile.txt' file.txt
```
**Example**:
```bash
sed '1r header.txt' data.txt
```
- Inserts the contents of `header.txt` after line 1 of `data.txt`.

---

#### **2.14. Write to a File (`w`)**
Write matching lines to a file.
```bash
sed -n '/error/w errors.txt' logfile.txt
```
**Example**:
```bash
sed -n '/404/w 404_errors.txt' access.log
```
- Writes all lines containing `404` to `404_errors.txt`.

---

#### **2.15. Quit (`q`)**
Exit after processing a specific line.
```bash
sed '10q' file.txt
```
**Example**:
```bash
sed '50q' largefile.txt
```
- Prints the first 50 lines and exits.

---

### **3. Advanced Examples**

#### **3.1. Remove Empty Lines**
```bash
sed '/^$/d' file.txt
```

#### **3.2. Remove Comments**
```bash
sed 's/#.*//' config.txt
```

#### **3.3. Double Space a File**
```bash
sed G file.txt
```

#### **3.4. Number Lines**
```bash
sed = file.txt | sed 'N;s/\n/\t/'
```

#### **3.5. Extract Email Addresses**
```bash
sed -n 's/.*\([a-zA-Z0-9._-]@[a-zA-Z0-9._-]\{2,\}.[a-zA-Z]\{2,\}\).*/\1/p' file.txt
```

---

### **4. Common Use Cases**
| Task                                  | Command                                                                 |
|---------------------------------------|-------------------------------------------------------------------------|
| Replace text                          | `sed 's/old/new/g' file.txt`                                          |
| Delete lines                          | `sed '/pattern/d' file.txt`                                            |
| Print specific lines                  | `sed -n '5,10p' file.txt`                                              |
| Insert/append text                    | `sed '3i\new line' file.txt`                                           |
| In-place editing                      | `sed -i 's/old/new/g' file.txt`                                        |
| Use regex                             | `sed -n '/^[A-Z]/p' file.txt`                                          |
| Extract content                       | `sed -n 's/.*\(pattern\).*/\1/p' file.txt`                              |

---

### **5. Tips and Tricks**
- **Backup Files**: Always back up files before using `-i`:
  ```bash
  sed -i.bak 's/old/new/g' file.txt
  ```
- **Test First**: Use `sed` without `-i` to preview changes.
- **Combine Commands**: Use `-e` for multiple operations.
- **Debugging**: Use `echo` and pipes to test patterns:
  ```bash
  echo "test" | sed 's/test/hello/'
  ```