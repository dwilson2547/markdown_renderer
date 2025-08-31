import argparse
from enum import Enum
import json
import logging
import os
import re
import sys
import stringcase as sc
from yattag import indent

LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}

logger = logging.getLogger("directory_scraper")
ch = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


class ResponseCode(Enum):
    INTERRUPT = -1
    ERROR = 1
    DONE = 0


content_dirname = "_contents_"
checksum_str = "checksum"

class FormatStrategy(Enum):
    LOCAL = "local"
    GITHUB = "github"

class DirectoryHomepagePageStragegy(Enum):
    INSIDE_DIRECTORY = "inside_directory"
    OUTSIDE_DIRECTORY = "outside_directory"

class StyleStrategy(Enum):
    BULLET = "bullet"
    NUMBERED = "numbered"
    DASHED = "dashed"

class SpacingStrategy(Enum):
    TWO = "two"
    FOUR = "four"
    EIGHT = "eight"

class TitleOptions(Enum):
    BOLD = "bold"
    UNDERLINE = "underline"
    CAMELCASE = "camelcase"
    PASCALCASE = "pascalcase"
    TITLECASE = "titlecase"
    STRIP_EXT = "strip_ext"
    UPPERCASE = "uppercase"
    LOWERCASE = "lowercase"
    SNAKECASE = "snakecase"


class DirectoryOptions(Enum):
    COLLAPSIBLE = "collapsible"
    FILES_FIRST = "files_first"
    FOLDERS_FIRST = "folders_first"
    DEFAULT_OPEN = "default_open"
    DEFAULT_CLOSED = "default_closed"
    DEFAULT_PARTIAL = "default_partial"


class HTMLClasses(Enum):
    DIRECTORY = "dir"
    FILE = "fil"
    DEAD_LINK = "deadlink"
    PAGE_NAV = "pagenav"

style = """
<style>
    ul {
        padding-left: 12px;
    }
    li {
        padding-left: 12px;
    }
    ul.bullet li.dir {
        list-style-type: circle
    }
    ul.bullet li.fil {
        list-style-type: disc;
    }
    ul.dashed li.dir {
        list-style-type: none;
    }
    ul.dashed li.fil {
        list-style-type: none;
    }
    ul.dashed li.fil::before {
        content: "-";

    }
    ul.dashed li.dir summary::before {
        content: "+";
    }
    ol {
        padding-left: 12px;
    }
    a.deadlink {
        font-weight: bold;
    }
    a.pagenav {
        text-decoration: underline;
    }
    summary {
        list-style: none; /* Ensures no default marker is shown */
        position: relative; /* Needed for absolute positioning of the custom arrow */
        padding-right: 20px; /* Adjust as needed to make space for the arrow */
        cursor: pointer; /* Indicates it's clickable */
    }

    summary::after {
        content: '▶'; /* Unicode character for a right-pointing triangle */
        transform: translateY(-50%); /* Vertically centers the arrow */
        transition: transform 0.2s ease-in-out;
    }

    details[open] summary::after {
        content: '▼'; /* Unicode character for a down-pointing triangle when open */
    }
</style>
"""

class SidebarBuidler:

    start_directory: str
    start_dir_len: int
    output_filename: str
    exclusions: list[str]
    default_exclusions: bool
    log_level: str
    verbose: bool
    format_strategy: str
    directoryHomepagePageStragegy: str
    styleStrategy: str
    titleOptions: list[str]
    directoryOptions: list[str]

    def __init__(
        self,
        start_directory: str,
        output_filename: str,
        exclusions: list[str],
        default_exclusions: bool,
        log_level: str,
        verbose: bool,
        format_strategy: str = FormatStrategy.LOCAL.value,
        directoryHomepagePageStragegy: str = DirectoryHomepagePageStragegy.INSIDE_DIRECTORY.value,
        stylestrategy: str = StyleStrategy.BULLET.value,
        spacingstrategy: str = SpacingStrategy.FOUR.value,
        titleOptions: list[str] = [
            TitleOptions.TITLECASE.value,
            TitleOptions.STRIP_EXT.value,
        ],
        directoryOptions: list[str] = [
            DirectoryOptions.COLLAPSIBLE.value,
            DirectoryOptions.FOLDERS_FIRST.value,
            DirectoryOptions.DEFAULT_PARTIAL.value,
        ],
    ) -> None:
        self.start_directory = start_directory
        self.output_filename = output_filename
        self.default_exclusions = default_exclusions
        self.log_level = log_level
        self.verbose = verbose
        self.format_strategy = format_strategy
        self.directoryHomepagePageStragegy = directoryHomepagePageStragegy
        self.styleStrategy = stylestrategy
        self.spacingstrategy = spacingstrategy
        self.titleOptions = titleOptions
        self.directoryOptions = directoryOptions

        if not self.start_directory:
            logger.info(
                "Failed to parse start directory. Re-run with -h flag to see help menu"
            )
            sys.exit(ResponseCode.ERROR.value)

        self.start_dir_len = len(os.path.split(self.start_directory.lstrip(os.sep)))

        if not self.output_filename:
            logger.info("No output filename provided, defaulting to sidebar.md")
            self.output_filename = "sidebar.md"
        if self.verbose:
            logger.setLevel(logging.DEBUG)
        elif log_level:
            if log_level.lower() in LOG_LEVELS:
                logger.setLevel(LOG_LEVELS[log_level])
        else:
            logger.setLevel(logging.INFO)

        self.exclusions = [
            re.compile("^" + re.escape(os.path.normpath(x)) + ".*") for x in exclusions
        ]
        if default_exclusions:
            default_excl = [
                ".git",
                "node_modules",
                "__pycache__",
                ".vscode",
                ".idea",
                ".DS_Store",
            ]
            self.exclusions += [
                re.compile(".*" + re.escape(x) + ".*") for x in default_excl
            ]

    def build_markdown_tree(self):
        """
        Builds tree of files to generate sidebar for
        """
        tree = {}

        for root, dirs, files in os.walk(self.start_directory):
            pos = tree
            if os.path.islink(root):
                continue
            should_skip = False
            for rgx in self.exclusions:
                if rgx.match(root):
                    should_skip = True
                    break
            if should_skip:
                continue
            for key in root.split(os.sep):
                if not key:
                    continue
                if not key in pos:
                    pos[key] = {content_dirname: []}
                pos = pos[key]
            for dir in dirs:
                should_skip = False
                for rgx in self.exclusions:
                    if rgx.match(dir):
                        should_skip = True
                        break
                if should_skip:
                    continue
                if not os.path.islink(os.path.join(root, dir)):
                    pos[dir] = {content_dirname: []}
            for file in files:
                if not self.file_is_markdown(file):
                    continue
                if os.path.isfile(os.path.join(root, file)):
                    pos[content_dirname].append(file)

        return tree

    def file_is_markdown(self, filename: str) -> bool:
        return filename.lower().endswith(".md") or filename.lower().endswith(
            ".markdown"
        )

    def unordered_list(self, content: str, html_class: str = None) -> str:
        return (
            "<ul>" + content + "</ul>"
            if not html_class
            else '<ul class="{}">'.format(html_class) + content + "</ul>"
        )

    def ordered_list(self, content: str, html_class: str = None) -> str:
        return (
            "<ol>" + content + "</ol>"
            if not html_class
            else '<ol class="{}">'.format(html_class) + content + "</ol>"
        )

    def list_item(self, content: str, html_class: str = None) -> str:
        return (
            "<li>" + content + "</li>"
            if not html_class
            else '<li class="{}">'.format(html_class) + content + "</li>"
        )

    def default_list(self, content: str, html_class: str = None) -> str:
        if self.styleStrategy == StyleStrategy.NUMBERED.value:
            return self.ordered_list(content, html_class)
        else:
            return self.unordered_list(content, html_class)

    def link(self, text: str, href: str, html_class: str = None) -> str:
        return '<a href="{}">{}</a>'.format(href, text) if not html_class else '<a class="{}" href="{}">{}</a>'.format(html_class, href, text)

    def dead_link(self, text: str, html_class: str = None) -> str:
        return "<a>{}</a>".format(text) if not html_class else '<a class="{}">{}</a>'.format(html_class, text)

    def summary(self, content: str) -> str:
        return "<summary>{}</summary>".format(content)

    def details(self, content: str, open: bool = True) -> str:
        if open:
            return "<details open>\n" + content + "\n</details>"
        else:
            return "<details>\n" + content + "\n</details>"

    def crawl_tree(
        self, tree: dict, output: list[str] = [], depth: int = 0, full_path: str = "/"
    ):
        for key_i, (key, value) in enumerate(tree.items()):
            if key == content_dirname:
                for file_i, file in enumerate(value):
                    rel_path = os.path.relpath(
                        os.path.join(full_path, file), start=self.start_directory
                    )
                    output.append(
                        self.format_file_link(
                            self.get_depth(rel_path),
                            file,
                            self.format_file_path(rel_path),
                            file_i,
                        )
                    )
            else:
                rel_path = os.path.relpath(
                    os.path.join(full_path, key), start=self.start_directory
                )
                if not rel_path.startswith("..") and rel_path != ".":
                    output.append(
                        self.format_directory_link(
                            self.get_depth(rel_path),
                            key,
                            self.format_directory_path(rel_path, key),
                            key_i,
                        )
                    )
                self.crawl_tree(
                    value, output, depth + 1, full_path=os.path.join(full_path, key)
                )
        return output

    def get_collapsible_state(self, depth: int) -> bool:
        if DirectoryOptions.DEFAULT_OPEN.value in self.directoryOptions:
            return True
        elif DirectoryOptions.DEFAULT_CLOSED.value in self.directoryOptions:
            return False
        elif DirectoryOptions.DEFAULT_PARTIAL.value in self.directoryOptions:
            return depth < 2
        else:
            return True

    def crawl_tree_collapsible(
        self, tree: dict, output: list[str] = [], depth: int = 0, full_path: str = "/"
    ):
        page_links = []
        file_links = []
        for key, value in tree.items():
            if key == content_dirname:
                for file in value:
                    rel_path = os.path.join(full_path, file)
                    file_links.append(
                        self.list_item(
                            self.link(
                                self.format_filename(file),
                                self.format_file_path(rel_path),
                            ),
                            HTMLClasses.FILE.value,
                        )
                    )
                if DirectoryOptions.FILES_FIRST.value in self.directoryOptions:
                    page_links += file_links
                    file_links = []
            else:
                rel_path = os.path.join(full_path, key)
                if not rel_path.startswith("..") and rel_path != ".":
                    page_links.append(
                        self.list_item(
                            self.details(
                                self.summary(
                                    self.dead_link(self.format_filename(key), HTMLClasses.DEAD_LINK.value)
                                    + " "
                                    + self.link(
                                        "(page)",
                                        self.format_directory_path(rel_path, key), HTMLClasses.PAGE_NAV.value)
                                )
                                + "\n"
                                + self.default_list(
                                    self.crawl_tree_collapsible(
                                        value,
                                        output,
                                        depth + 1,
                                        full_path=os.path.join(full_path, key),
                                    )
                                )
                                + "\n",
                                self.get_collapsible_state(depth),
                            ), HTMLClasses.DIRECTORY.value
                        )
                    )
        if DirectoryOptions.FOLDERS_FIRST.value in self.directoryOptions:
            page_links = page_links + file_links
        if depth == 0:
            return self.default_list("".join(page_links), html_class=self.styleStrategy)
        return self.default_list("".join(page_links))

    def get_depth(self, path: str) -> int:
        return len([x for x in path.split(os.sep) if x != ""]) - 1

    def format_filename(self, filename: str) -> str:
        temp = filename
        if TitleOptions.STRIP_EXT.value in self.titleOptions:
            temp = temp.rsplit(".", 1)[0]
        if TitleOptions.CAMELCASE.value in self.titleOptions:
            temp = sc.camelcase(temp)
        if TitleOptions.PASCALCASE.value in self.titleOptions:
            temp = sc.pascalcase(temp)
        if TitleOptions.TITLECASE.value in self.titleOptions:
            temp = sc.titlecase(temp)
        if TitleOptions.UPPERCASE.value in self.titleOptions:
            temp = temp.upper()
        if TitleOptions.LOWERCASE.value in self.titleOptions:
            temp = temp.lower()
        if TitleOptions.SNAKECASE.value in self.titleOptions:
            temp = sc.snakecase(temp)
        if TitleOptions.BOLD.value in self.titleOptions:
            temp = "**{}**".format(temp)
        if TitleOptions.UNDERLINE.value in self.titleOptions:
            temp = "__{}__".format(temp)
        return temp

    def format_file_path(self, relative_path: str) -> str:
        if self.format_strategy == FormatStrategy.LOCAL.value:
            return os.path.join("./", relative_path)

    def format_directory_path(self, relative_path: str, key: str) -> str:
        if self.format_strategy == FormatStrategy.LOCAL.value:
            if (
                self.directoryHomepagePageStragegy
                == DirectoryHomepagePageStragegy.INSIDE_DIRECTORY.value
            ):
                return os.path.join("./", relative_path, key, key + ".md")
            elif (
                self.directoryHomepagePageStragegy
                == DirectoryHomepagePageStragegy.OUTSIDE_DIRECTORY.value
            ):
                return os.path.join("./", relative_path, key + ".md")

    def style_denominator(self, style: str, index: int = 0) -> str:
        if style == StyleStrategy.BULLET.value:
            return "*"
        elif style == StyleStrategy.DASHED.value:
            return "-"
        elif style == StyleStrategy.NUMBERED.value:
            return "{}.".format(index + 1)
        else:
            return "*"

    def get_style_denominator(self, index: int = 0) -> str:
        return self.style_denominator(self.styleStrategy, index=index)

    def spacing_string(self) -> str:
        if self.spacingstrategy == SpacingStrategy.TWO.value:
            return "  "
        elif self.spacingstrategy == SpacingStrategy.FOUR.value:
            return "    "
        elif self.spacingstrategy == SpacingStrategy.EIGHT.value:
            return "        "
        else:
            return "    "

    def format_title(self, title: str) -> str:
        if TitleOptions.CAMELCASE.value in self.titleOptions:
            title = re.sub(r"(_|-)+", " ", title).title().replace(" ", "")
        if TitleOptions.STRIP_EXT.value in self.titleOptions:
            title = re.sub(r"\.md$|\.markdown$", "", title, flags=re.IGNORECASE)
        if TitleOptions.BOLD.value in self.titleOptions:
            title = "**{}**".format(title)
        if TitleOptions.UNDERLINE.value in self.titleOptions:
            title = "__{}__".format(title)
        return title

    def format_directory_link(
        self, depth: int, text: str, path: str, index: int
    ) -> str:
        denom = self.get_style_denominator(index)
        return "{}{} [{}]({})\n".format(
            self.spacing_string() * depth, denom, self.format_filename(text), path
        )

    def format_file_link(self, depth: int, text: str, path: str, index: int) -> str:
        denom = self.get_style_denominator(index)
        return "{}{} [{}]({})\n".format(
            self.spacing_string() * depth, denom, self.format_filename(text), path
        )

    def save_collapsible_sidebar(self, text: str, output_filename: str):
        with open(output_filename, "w") as f:
            f.write(text)

    def save_sidebar(self, sidebar_lines: list[str], output_filename: str):
        with open(output_filename, "w") as f:
            f.write("\n".join(sidebar_lines))

    def start(self):
        tree = self.build_markdown_tree()

        for part in self.start_directory.split(os.sep):
            if part in tree:
                tree = tree[part]

        if DirectoryOptions.COLLAPSIBLE.value not in self.directoryOptions:
            sidebar_lines = self.crawl_tree(tree)
            self.save_sidebar(sidebar_lines, self.output_filename)
        else:
            sidebar_lines = self.crawl_tree_collapsible(tree)
            sidebar_lines = style + "\n" + sidebar_lines
            # root = html.fromstring(sidebar_lines)
            # pretty_html = etree.tostring(root, pretty_print=True, encoding='unicode')
            pretty_html = indent(
                sidebar_lines, indentation="    ", newline="\n", indent_text=True
            )
            self.save_collapsible_sidebar(pretty_html, self.output_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Sidebar Builder", description="", epilog="epilog"
    )

    parser.add_argument(
        "-o",
        "--output-filename",
        help="Filename to save output to, ie. python3 script.py -o sidebar.md",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose debugging"
    )
    parser.add_argument(
        "-e",
        "--exclude",
        nargs="*",
        help="Paths to exclude, ie. python3 script.py -o sidebar.md -e /directory/to/scan/subpath/to/ignore -s /directory/to/scan",
    )
    parser.add_argument(
        "-de",
        "--default-exclusions",
        action="store_true",
        help="Enable default exclusions, ie. .git, node_modules, etc.",
    )
    parser.add_argument(
        "-ll",
        "--log-level",
        help="Hard override to the global log level, available: [debug, info, warning, error]",
    )
    parser.add_argument(
        "-s",
        "--start-directory",
        help="Directory to scan for markdown files in, ie. python3 script.py -o sidebar.md -s /directory/to/scan",
    )

    args = parser.parse_args()

    start_directory: str = args.start_directory if args.start_directory else os.getcwd()
    output_filename: list[str] = args.output_filename if args.output_filename else None
    exclusions: list[str] = args.exclude if args.exclude else []
    default_exclusions: bool = (
        args.default_exclusions if args.default_exclusions else True
    )
    log_level: str = args.log_level if args.log_level else None
    verbose: bool = args.verbose if args.verbose else None

    sidebarBuilder = SidebarBuidler(
        start_directory,
        output_filename,
        exclusions,
        default_exclusions,
        log_level,
        verbose,
    )

    sidebarBuilder.start()
