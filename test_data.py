import csv,unittest
from pathlib import Path
class TestAds(unittest.TestCase):
 def test_15_ads_and_five_per_style(self):
  p=Path(__file__).parents[1]/"data/ad_variants.csv"
  with p.open(encoding="utf-8") as f: rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),15)
  self.assertEqual({s:sum(r["prompt_style"]==s for r in rows) for s in ["Basic","Role-based","Few-shot"]},{"Basic":5,"Role-based":5,"Few-shot":5})
if __name__=="__main__": unittest.main()
