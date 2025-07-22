from rich.console import Console
from rich.theme import Theme

# Define color theme
custom_theme = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "bold red",
    "title": "bold magenta",
})

# Create console with theme
console = Console(theme=custom_theme)

# Logging functions
def log_info(message):
    console.print(f"[INFO] {message}", style="info")

def log_success(message):
    console.print(f"[✓] {message}", style="success")

def log_warning(message):
    console.print(f"[!] {message}", style="warning")

def log_error(message):
    console.print(f"[✗] {message}", style="error")

def log_title(message):
    console.print(f"\n=== {message} ===", style="title")
