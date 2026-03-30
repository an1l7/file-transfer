from scraper.ui import get_user_input
from scraper.utils import generate_progress_filename, get_last_progress
from scraper.core import run_scraper

def main():
    base_url, output_file = get_user_input()
    progress_file = generate_progress_filename(base_url)

    _, last_url, _ = get_last_progress(progress_file)

    run_scraper(base_url, output_file, progress_file, last_url)

if __name__ == "__main__":
    main()
    