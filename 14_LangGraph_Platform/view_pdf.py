#!/usr/bin/env python3
"""Simple utility to view PDF files in the terminal."""

import sys
from pathlib import Path
import pymupdf  # PyMuPDF


def view_pdf(pdf_path: str, page_start: int = 1, page_end: int | None = None):
    """
    Extract and display text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        page_start: First page to display (1-indexed)
        page_end: Last page to display (1-indexed), None for all pages
    """
    pdf_file = Path(pdf_path)
    
    if not pdf_file.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        return
    
    try:
        # Open the PDF
        doc = pymupdf.open(pdf_file)
        total_pages = len(doc)
        
        print(f"\n{'='*80}")
        print(f"PDF: {pdf_file.name}")
        print(f"Total Pages: {total_pages}")
        print(f"{'='*80}\n")
        
        # Adjust page range (convert from 1-indexed to 0-indexed)
        start_idx = max(0, page_start - 1)
        end_idx = min(total_pages, page_end) if page_end else total_pages
        
        # Extract and display text from each page
        for page_num in range(start_idx, end_idx):
            page = doc[page_num]
            text = page.get_text()
            
            print(f"\n{'─'*80}")
            print(f"Page {page_num + 1} of {total_pages}")
            print(f"{'─'*80}\n")
            print(text)
        
        doc.close()
        
        print(f"\n{'='*80}")
        print(f"End of PDF (displayed pages {start_idx + 1}-{end_idx})")
        print(f"{'='*80}\n")
        
    except Exception as e:
        print(f"Error reading PDF: {e}")


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python view_pdf.py <pdf_file> [start_page] [end_page]")
        print("\nExample:")
        print("  python view_pdf.py data/howpeopleuseai.pdf")
        print("  python view_pdf.py data/howpeopleuseai.pdf 1 5")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    page_start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    page_end = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    view_pdf(pdf_path, page_start, page_end)


if __name__ == "__main__":
    main()

