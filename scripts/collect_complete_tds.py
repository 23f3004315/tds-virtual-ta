#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.collectors.course_collector import TDSCourseCollector
from src.collectors.tds_discourse_posts_collector import TDSPostsCollector

def main():
    parser = argparse.ArgumentParser(description="Complete TDS Data Collection")
    parser.add_argument("--start-date", default="2025-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default="2025-04-14", help="End date (YYYY-MM-DD)")
    parser.add_argument("--course-only", action="store_true", help="Course content only")
    parser.add_argument("--discourse-only", action="store_true", help="Discourse posts only")
    
    args = parser.parse_args()
    
    print("COMPLETE TDS DATA COLLECTION")
    print("=" * 60)
    print(f"Date range: {args.start_date} to {args.end_date}")
    
    if not args.discourse_only:
        print("\nCOURSE CONTENT COLLECTION")
        course_collector = TDSCourseCollector()
        course_files = course_collector.collect_all_course_content()
        print(f"Course: {len(course_files)} files")
    
    if not args.course_only:
        print("\nTDS DISCOURSE COLLECTION")
        complete_collector = TDSPostsCollector()
        stats = complete_collector.collect_complete_tds_data(
            start_date=args.start_date,
            end_date=args.end_date
        )
    
    print("\nCOLLECTION COMPLETE!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
