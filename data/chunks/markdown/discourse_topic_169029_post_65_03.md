---
chunk_id: discourse_topic_169029_post_65_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/65
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 153
username: 23f2004837
post_number: 65
topic_id: 169029
---

 if success:
 logging.info(f"✅ {use_case} PASSED")
 else:
 logging.error(f"❌ {use_case} FAILED")
 a_score += 1 if success else 0
 
 logging.info(f"🎯 Parsed: {a_score} / {a_total}")

---

if __name__ == "__main__":
 import asyncio
 import argparse

parser = argparse.ArgumentParser(description="Evaluate GA No with configurable logging")
 levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
 parser.add_argument("--log-level", default="INFO", choices=levels, help="Set logging level")
 args = parser.parse_args()
 logging.basicConfig(level=args.log_level, format="%(message)s\n")
 
 asyncio.run(main())

`
