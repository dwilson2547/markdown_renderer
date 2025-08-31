Here’s a **comprehensive `grep` cheat sheet** with common commands and practical examples:

---

### **`grep` Cheat Sheet**
`grep` (Global Regular Expression Print) is a powerful Linux command for searching text and patterns in files.

---

- [**`grep` Cheat Sheet**](#grep-cheat-sheet)
- [**1. Basic Syntax**](#1-basic-syntax)
- [**2. Common Options**](#2-common-options)
- [**3. Basic Searches**](#3-basic-searches)
  - [**3.1. Search for a String**](#31-search-for-a-string)
  - [**3.2. Case-Insensitive Search**](#32-case-insensitive-search)
  - [**3.3. Count Matches**](#33-count-matches)
  - [**3.4. Show Line Numbers**](#34-show-line-numbers)
  - [**3.5. Invert Match (Exclude)**](#35-invert-match-exclude)
  - [**3.6. Search in Multiple Files**](#36-search-in-multiple-files)
  - [**3.7. Recursive Search in Directories**](#37-recursive-search-in-directories)
  - [**3.8. Whole Word Match**](#38-whole-word-match)
  - [**3.9. Show Context Around Matches**](#39-show-context-around-matches)
- [**4. Advanced Searches with Regex**](#4-advanced-searches-with-regex)
  - [**4.1. Match Lines Starting with a Pattern**](#41-match-lines-starting-with-a-pattern)
  - [**4.2. Match Lines Ending with a Pattern**](#42-match-lines-ending-with-a-pattern)
  - [**4.3. Match Specific Patterns**](#43-match-specific-patterns)
  - [**4.4. Extended Regex (`-E`)**](#44-extended-regex--e)
  - [**4.5. Match Email Addresses**](#45-match-email-addresses)
  - [**4.6. Match IP Addresses**](#46-match-ip-addresses)
- [**5. Practical Examples**](#5-practical-examples)
  - [**5.1. Find Files Containing a Pattern**](#51-find-files-containing-a-pattern)
  - [**5.2. Search in Compressed Files**](#52-search-in-compressed-files)
  - [**5.3. Pipe Output to `grep`**](#53-pipe-output-to-grep)
  - [**5.4. Search in Command Output**](#54-search-in-command-output)
  - [**5.5. Highlight Matches**](#55-highlight-matches)
  - [**5.6. Search for Empty Lines**](#56-search-for-empty-lines)
  - [**5.7. Search for Lines with Only Numbers**](#57-search-for-lines-with-only-numbers)
- [**6. Common Use Cases**](#6-common-use-cases)
- [**7. Tips and Tricks**](#7-tips-and-tricks)


### **1. Basic Syntax**
```bash
grep [options] "pattern" [file]
```

---

### **2. Common Options**

| Option | Description                          | Example                                      |
|--------|--------------------------------------|----------------------------------------------|
| `-i`   | Case-insensitive search              | `grep -i "error" logfile.txt`                |
| `-v`   | Invert match (exclude pattern)       | `grep -v "success" logfile.txt`              |
| `-n`   | Show line numbers                    | `grep -n "warning" logfile.txt`              |
| `-c`   | Count matching lines                 | `grep -c "404" access.log`                   |
| `-r`   | Recursive search (directories)       | `grep -r "function" /path/to/dir/`           |
| `-l`   | List files with matches              | `grep -l "main()" *.c`                       |
| `-w`   | Match whole words only               | `grep -w "port" config.txt`                  |
| `-A n` | Show `n` lines after match           | `grep -A 3 "error" logfile.txt`              |
| `-B n` | Show `n` lines before match          | `grep -B 2 "error" logfile.txt`              |
| `-C n` | Show `n` lines around match          | `grep -C 1 "error" logfile.txt`              |
| `-E`   | Extended regex (use with `|`, `+`, etc.) | `grep -E "error|warning" logfile.txt`    |
| `-F`   | Fixed string (no regex)              | `grep -F "this exact string" file.txt`       |
| `--color` | Highlight matches                | `grep --color "pattern" file.txt`            |

---

### **3. Basic Searches**

#### **3.1. Search for a String**
```bash
grep "pattern" file.txt
```
**Example**:
```bash
grep "hello" example.txt
```
- Searches for `hello` in `example.txt`.

---

#### **3.2. Case-Insensitive Search**
```bash
grep -i "pattern" file.txt
```
**Example**:
```bash
grep -i "error" logfile.txt
```
- Matches `error`, `Error`, `ERROR`, etc.

---

#### **3.3. Count Matches**
```bash
grep -c "pattern" file.txt
```
**Example**:
```bash
grep -c "404" access.log
```
- Counts how many times `404` appears in `access.log`.

---

#### **3.4. Show Line Numbers**
```bash
grep -n "pattern" file.txt
```
**Example**:
```bash
grep -n "warning" system.log
```
- Shows line numbers where `warning` appears.

---

#### **3.5. Invert Match (Exclude)**
```bash
grep -v "pattern" file.txt
```
**Example**:
```bash
grep -v "success" results.txt
```
- Shows lines that **do not** contain `success`.

---

#### **3.6. Search in Multiple Files**
```bash
grep "pattern" file1.txt file2.txt
```
**Example**:
```bash
grep "TODO" *.py
```
- Searches for `TODO` in all `.py` files.

---

#### **3.7. Recursive Search in Directories**
```bash
grep -r "pattern" /path/to/dir/
```
**Example**:
```bash
grep -r "include" /usr/include/
```
- Recursively searches for `include` in `/usr/include/`.

---

#### **3.8. Whole Word Match**
```bash
grep -w "word" file.txt
```
**Example**:
```bash
grep -w "port" config.txt
```
- Matches `port` but not `report` or `export`.

---

#### **3.9. Show Context Around Matches**
```bash
grep -A 2 -B 2 "pattern" file.txt
```
**Example**:
```bash
grep -A 3 -B 1 "error" logfile.txt
```
- Shows 1 line before and 3 lines after each match.

---

### **4. Advanced Searches with Regex**

#### **4.1. Match Lines Starting with a Pattern**
```bash
grep "^pattern" file.txt
```
**Example**:
```bash
grep "^#" script.sh
```
- Finds lines starting with `#` (comments).

---

#### **4.2. Match Lines Ending with a Pattern**
```bash
grep "pattern$" file.txt
```
**Example**:
```bash
grep ";$" script.sh
```
- Finds lines ending with `;`.

---

#### **4.3. Match Specific Patterns**
```bash
grep "[0-9]" file.txt       # Lines with numbers
grep "[A-Za-z]" file.txt    # Lines with letters
grep "a.*b" file.txt        # Lines with `a` followed by `b`
```
**Example**:
```bash
grep "^[A-Z]" names.txt
```
- Finds lines starting with a capital letter.

---

#### **4.4. Extended Regex (`-E`)**
```bash
grep -E "pattern1|pattern2" file.txt
```
**Example**:
```bash
grep -E "error|fail|warning" logfile.txt
```
- Matches `error`, `fail`, or `warning`.

---

#### **4.5. Match Email Addresses**
```bash
grep -E "[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+" file.txt
```
**Example**:
```bash
grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b" contacts.txt
```
- Extracts email addresses.

---

#### **4.6. Match IP Addresses**
```bash
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" file.txt
```
**Example**:
```bash
grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" access.log
```
- Extracts IPv4 addresses.

---

### **5. Practical Examples**

#### **5.1. Find Files Containing a Pattern**
```bash
grep -l "main()" *.c
```
- Lists all `.c` files containing `main()`.

---

#### **5.2. Search in Compressed Files**
```bash
zgrep "pattern" file.gz
```
**Example**:
```bash
zgrep "error" archive.log.gz
```
- Searches inside a `.gz` file.

---

#### **5.3. Pipe Output to `grep`**
```bash
command | grep "pattern"
```
**Example**:
```bash
dmesg | grep -i "usb"
```
- Filters `dmesg` output for USB-related messages.

---

#### **5.4. Search in Command Output**
```bash
ps aux | grep "nginx"
```
- Finds processes related to `nginx`.

---

#### **5.5. Highlight Matches**
```bash
grep --color "pattern" file.txt
```
**Example**:
```bash
grep --color "TODO" notes.txt
```
- Highlights `TODO` in the output.

---

#### **5.6. Search for Empty Lines**
```bash
grep "^$" file.txt
```
- Finds empty lines.

---

#### **5.7. Search for Lines with Only Numbers**
```bash
grep "^[0-9]*$" file.txt
```
- Matches lines with only numbers.

---

### **6. Common Use Cases**

| Task                                      | Command                                      |
|-------------------------------------------|----------------------------------------------|
| Search for a string                       | `grep "text" file.txt`                       |
| Case-insensitive search                   | `grep -i "text" file.txt`                    |
| Count matches                             | `grep -c "pattern" file.txt`                 |
| Recursive search                          | `grep -r "pattern" /path/`                   |
| Exclude a pattern                         | `grep -v "pattern" file.txt`                 |
| Show line numbers                         | `grep -n "pattern" file.txt`                 |
| Whole word match                          | `grep -w "word" file.txt`                    |
| Search with regex                         | `grep -E "pattern1|pattern2" file.txt`      |
| Search in compressed files                | `zgrep "pattern" file.gz`                    |
| Pipe output to `grep`                     | `ls -l | grep "Aug"`                              |

---

### **7. Tips and Tricks**
- **Combine with `find`**:
  ```bash
  find /var/log -type f -exec grep -l "error" {} \;
  ```
- **Use `grep` with `xargs`**:
  ```bash
  grep -rl "old-text" /path/ | xargs sed -i 's/old-text/new-text/g'
  ```
- **Save results to a file**:
  ```bash
  grep "pattern" file.txt > results.txt
  ```
- **Search in `less`**:
  Press `/` in `less` to search interactively.