from raducord import Console, Logger
from colorama import Fore, Back, Style, init
import instaloader
from concurrent.futures import ThreadPoolExecutor
import json
import time
import os
import os.path
import pickle
from datetime import datetime
import sys
from time import sleep
import random
import threading
from typing import List, Optional
import shutil

init(autoreset=True)

class Colors:
    PRIMARY = Fore.CYAN
    SECONDARY = Fore.MAGENTA
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    INFO = Fore.BLUE
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT

class Animation:
    @staticmethod
    def loading(message: str, duration: float = 0.5):
        """Display a loading animation with a message"""
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f"\r                                               {Colors.INFO}{frames[i]} {message}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
            i = (i + 1) % len(frames)
        sys.stdout.write("\r                                               " + " " * (len(message) + 2) + "\r")
        sys.stdout.flush()

    @staticmethod
    def print_slow(text: str, delay: float = 0.03, center: bool = True):
        """Print text with a typewriter effect, optionally centered"""
        terminal_width = shutil.get_terminal_size().columns
        if center:
            lines = text.split('\n')
            for line in lines:
                visible_length = len(line.replace(Colors.PRIMARY, '').replace(Colors.SECONDARY, '')
                                  .replace(Colors.INFO, '').replace(Colors.RESET, ''))
                padding = (terminal_width - visible_length) // 2
                centered_line = ' ' * padding + line
                for char in centered_line:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(delay)
                sys.stdout.write('\n')
        else:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print()

class UI:
    @staticmethod
    def clear():
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def center_text(text: str) -> str:
        """Center text in terminal"""
        terminal_width = shutil.get_terminal_size().columns
        lines = text.split('\n')
        centered_lines = []
        for line in lines:
            if line.strip():
                visible_length = len(line.replace(Colors.PRIMARY, '').replace(Colors.SECONDARY, '')
                                   .replace(Colors.INFO, '').replace(Colors.RESET, ''))
                padding = (terminal_width - visible_length) // 2
                centered_lines.append(' ' * padding + line)
            else:
                centered_lines.append(line)
        return '\n'.join(centered_lines)

    @staticmethod
    def print_banner():
        """Print the application banner with animation"""
        banner = f"""
                                        {Colors.PRIMARY}╔═══════════════════════════════════════════╗
                                        ║  {Colors.SECONDARY}Instagram Tool{Colors.PRIMARY} by {Colors.INFO}thee0x91{Colors.PRIMARY}               ║
                                        ╚═══════════════════════════════════════════╝{Colors.RESET}
"""
        print(banner)

    @staticmethod
    def print_menu():
        """Print the main menu with animation"""
        menu = f"""
                                                ╔═════════════════════╗
                                                ║  {Colors.SECONDARY}Select Option{Colors.PRIMARY}      ║
                                                ╠═════════════════════╣
                                                ║                     ║
                                                ║  {Colors.INFO}[1]{Colors.RESET} Story Loader   ║
                                                ║  {Colors.INFO}[2]{Colors.RESET} Check Following║
                                                ║  {Colors.INFO}[3]{Colors.RESET} Exit           ║
                                                ║                     ║
                                                ╚═════════════════════╝{Colors.RESET}
"""
        print(menu)

    @staticmethod
    def input_styled(prompt: str) -> str:
        """Get user input with styled prompt"""
        return input(f"                                               {Colors.PRIMARY}❯ {Colors.SECONDARY}{prompt}{Colors.RESET}")

    @staticmethod
    def print_status(message: str, status: str = "info"):
        """Print a status message with appropriate styling"""
        color = getattr(Colors, status.upper(), Colors.INFO)
        prefix = {
            "success": "✓",
            "error": "✗",
            "warning": "⚠",
            "info": "ℹ"
        }.get(status.lower(), "•")
        print(f"                                               {color}{prefix} {message}{Colors.RESET}")

    @staticmethod
    def print_section(title: str):
        """Print a section header"""
        print(f"\n                                               {Colors.PRIMARY}=== {Colors.SECONDARY}{title}{Colors.PRIMARY} ==={Colors.RESET}\n")

class InstagramTool:
    SESSION_FILE = "session.pkl"
    
    @staticmethod
    def save_session(L):
        """Save session to file"""
        try:
            with open(InstagramTool.SESSION_FILE, 'wb') as f:
                session_data = {
                    'cookies': L.context._session.cookies
                }
                pickle.dump(session_data, f)
        except:
            pass

    @staticmethod
    def load_session(L):
        """Load session from file"""
        try:
            with open(InstagramTool.SESSION_FILE, 'rb') as f:
                session_data = pickle.load(f)
                L.context._session.cookies.update(session_data['cookies'])
            return True
        except:
            return False

    @staticmethod
    def login_to_instagram():
        """Login to Instagram and return Instaloader instance"""
        try:
            L = instaloader.Instaloader(max_connection_attempts=1)
            
            config = InstagramTool.load_config()
            if not config:
                UI.print_status("Failed to load config.json", "error")
                return None
                
            username = config.get('USERNAME')
            password = config.get('PASSWORD')
            
            if not username or not password:
                UI.print_status("Missing USERNAME or PASSWORD in config.json", "error")
                return None

            session_file = f"{username}_session"
            if os.path.exists(session_file):
                try:
                    L.load_session_from_file(username, session_file)
                    if InstagramTool.verify_login(L, username):
                        UI.print_status("Successfully loaded saved session", "success")
                        return L
                except Exception:
                    if os.path.exists(session_file):
                        os.remove(session_file)
            
            try:
                UI.print_status("Logging in with credentials...", "info")
                L.login(username, password)
                L.save_session_to_file(session_file)
                if InstagramTool.verify_login(L, username):
                    UI.print_status("Successfully logged in", "success")
                    return L
                else:
                    UI.print_status("Login failed - session verification error", "error")
                    return None
            except Exception as e:
                UI.print_status(f"Login failed: {str(e)}", "error")
                return None
                
        except Exception as e:
            UI.print_status(f"Login error: {str(e)}", "error")
            return None
            
        return None

    @staticmethod
    def verify_login(L, username):
        """Verify if the login session is valid"""
        try:
            profile = instaloader.Profile.from_username(L.context, username)
            profile.get_posts()  
            return True
        except Exception:
            return False

    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            UI.print_status(f"Error loading config: {str(e)}", "error")
            return None

    @staticmethod
    def codemenu():
        while True:
            UI.clear()
            UI.print_banner()
            print("\n")  
            UI.print_menu()
            print("\n")  
            
            choice = UI.input_styled("Select an option (1-3): ")
            
            if choice == '1':
                UI.clear()
                Animation.loading("Loading Story Loader", 1)
                InstagramTool.Storyloader()
            elif choice == '2':
                UI.clear()
                Animation.loading("Loading Following Checker", 1)
                InstagramTool.checkfollowing()
            elif choice == '3':
                UI.clear()
                UI.print_status("Thank you for using Instagram Tool!", "success")
                UI.print_status("Goodbye!", "info")
                time.sleep(1)
                sys.exit(0)
            else:
                UI.print_status("Invalid option. Please select 1-3", "error")
                time.sleep(1)

    @staticmethod
    def Storyloader():
        L = InstagramTool.login_to_instagram()
        if not L:
            UI.print_status("Failed to login. Please check your credentials in config.json", "error")
            time.sleep(2)
            InstagramTool.codemenu()
            return

        UI.print_section("Story Loader")

        target_username = UI.input_styled("Enter the target username: ")
        
        try:
            profile = instaloader.Profile.from_username(L.context, target_username)
        except Exception as e:
            UI.print_status(f"Failed to find profile: {str(e)}", "error")
            time.sleep(2)
            InstagramTool.codemenu()
            return

        UI.print_section("Download Options")

        download_posts = UI.input_styled("Download posts? (y/n): ").lower() == 'y'
        download_highlights = UI.input_styled("Download highlights? (y/n): ").lower() == 'y'
        download_stories = UI.input_styled("Download stories? (y/n): ").lower() == 'y'

        log_filename = f"log/Storyloader/{target_username}.txt"
        os.makedirs(os.path.dirname(log_filename), exist_ok=True)

        with open(log_filename, 'w') as log_file:
            def log(msg):
                UI.print_status(msg, "info")
                log_file.write(msg + '\n')

            def download_storyitem(item, target):
                try:
                    L.download_storyitem(item, target=target)
                    log(f"Downloaded story item {item} to {target}")
                except Exception as e:
                    log(f"Error downloading story item: {e}")

            def download_post(post, target):
                try:
                    L.download_post(post, target=target)
                    log(f"Downloaded post {post} to {target}")
                except Exception as e:
                    log(f"Error downloading post: {e}")

            UI.print_section("Starting Download")

            if download_stories:
                Animation.loading("Downloading stories", 1)
                with ThreadPoolExecutor() as executor:
                    for story in L.get_stories(userids=[profile.userid]):
                        executor.map(lambda item: download_storyitem(item, target=profile.username), story.get_items())

            if download_highlights:
                Animation.loading("Downloading highlights", 1)
                with ThreadPoolExecutor() as executor:
                    for highlight in L.get_highlights(profile):
                        executor.map(lambda item: download_storyitem(item, target=f"{profile.username}_highlights"), highlight.get_items())

            if download_posts:
                Animation.loading("Downloading posts", 1)
                with ThreadPoolExecutor() as executor:
                    executor.map(lambda post: download_post(post, target=f"{profile.username}_posts"), profile.get_posts())

            UI.print_section("Download Complete")
            UI.print_status(f"Successfully downloaded content for {target_username}", "success")
            Logger.success(f"Success Download,Instagram tool,{target_username}")

        time.sleep(2)
        InstagramTool.codemenu()

    @staticmethod
    def checkfollowing():
        L = InstagramTool.login_to_instagram()
        if not L:
            UI.print_status("Failed to login. Please check your credentials in config.json", "error")
            time.sleep(2)
            InstagramTool.codemenu()
            return

        UI.print_section("Following Checker")

        target_username = UI.input_styled("Enter the target username to check: ")
        
        try:
            profile = instaloader.Profile.from_username(L.context, target_username)
        except Exception as e:
            UI.print_status(f"Failed to find profile: {str(e)}", "error")
            time.sleep(2)
            InstagramTool.codemenu()
            return

        log_filename = f"log/checkfollowing/{target_username}.txt"
        os.makedirs(os.path.dirname(log_filename), exist_ok=True)

        with open(log_filename, 'w') as log_file:
            def log(msg):
                UI.print_status(msg, "info")
                log_file.write(msg + '\n')

            Animation.loading("Fetching following list", 1)
            following = set(profile.get_followees())
            
            Animation.loading("Fetching followers list", 1)
            followers = set(profile.get_followers())

            UI.print_section("Users Not Following Back")

            not_following_back = following - followers
            for user in not_following_back:
                log(user.username)

            UI.print_section("Check Complete")
            UI.print_status(f"Successfully checked following for {target_username}", "success")
            Logger.success(f"Success Check,Instagram tool,{target_username}")

        time.sleep(2)
        InstagramTool.codemenu()

config = json.load(open("config.json"))

main = InstagramTool
main.codemenu()
