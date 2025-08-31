# Regex find and Replace
The greatest thing since sliced bread, or at least very nearly. Most decent text editors come with regex find and replace built in. I will be demonstrating with **[VSCode](../core_concepts/development/tools/ide.md)** and **[Sublime Text](../core_concepts/development/tools/text_editors.md)** but I believe [Notepad++](https://notepad-plus-plus.org/) supports this too. 

## Find and replace modes

### VSCode and Sublime

* Standard - Standard find and replace, case insensitive 
* Match Case - Standard but case sensitive
* Whole word - Will not match partial word, ie. searching 'sea' against text 'seal' will return no result, but searching 'seal' will
* Regex - Regular expression 

# Regex Find

# Regex Replace

You can wrap clauses of a regex find in parenthesis to create groups witin the search text, and then you can reference those groups in the replace bar to re-organize the strings. Groups are referenced with the `$` character, followed by the integer that represents that groups position in the find pattern, starting with 1.

## Remove Pattern Example

You've just copied a block of text from wikipedia and want to remove the reference markers from the data. You could do this manually but a regex find and replace makes this very quick and easy. Below is an example of what a reference marker from wikipedia might look like: 

> some text [[2]](#)

So we want to remve that [2], but there could be other references that are different numbers as well. To fix this, we'll write a pattern to identify these references, and replace them with nothing

Search Pattern: \[([0-9]+)\]
Replace Pattern: ""

![](/dev_tips/pictures/regex_remove_pattern_match_results.png)

Result:
> some text

## Replace Pattern Example

You have a long list of file paths that are being fed to an application, but an error occurred while generating the list and two of the directory names got flipped. The file paths should start with /home/user, but instead they start with /user/home. To fix this, we'll write a pattern that creates groups from the first two directories, and then we'll flip those groups in the output. 

Example Text: 
> [/user/home/documents/readme.md](../../user/home/documents/readme.md) <br>
  /user/home/.pip/pip.conf <br>
  /user/home/.m2/settings.xml

Search Pattern: ^\/([\w]+)\/([\w]+)\/(.*)
Explanation: 
1. ^ means starting from the beginning, so it will always grab the first two directories
2. The / character must be escaped by the \ character, so \/ will match / in the directory string
3. \w matches word characters (letters), and + means get all characters that match that description in a row, so the directory name is returned
4. . matches anything and * matches any length, so this just makes it match the rest of the string

Results: 

![](/dev_tips/pictures/regex_replace_pattern_match_results.png)

Now if we set the replace string to this, we will reverse the first two directories:

` /$2/$1/$3 `

Results: 

> [/home/user/documents/readme.md](../../home/user/documents/readme.md) <br>
  /home/user/.pip/pip.conf <br>
  /home/user/.m2/settings.xml