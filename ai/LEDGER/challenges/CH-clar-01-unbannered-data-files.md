# CH-clar-01-unbannered-data-files

**TL;DR.** The new unpublished-vs-`main` banners cover the markdown writeups and scripts, but not the branch-only data files sitting next to them. A reviewer who opens a CSV, JSON, or source excerpt under `Release/Examples/` still sees no notice that the file is not on `main`.

- **Claim:** C-clar-01
- **Challenge:** C-clar-01 says diverging and branch-only `Release/` files carry an unpublished-vs-`main` banner, and names a falsifier if a diverging `Release/` file still has no such notice. Markdown entry points and scripts were bannered. The following added data files were not, because a markdown banner would break the format — but they also have no folder-level notice of their own:

  - `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`
  - Every `outputs/` and `sources/` file under the four worked-fill trees (Tulare Lake, Keokuk / LD19, Niger precip, Niger cereal yield): CSVs, JSON, GeoJSON, `.rdb`, `.html`, and source excerpts.

  A parent `WORKED_FILL.md` or `NOTES.md` is bannered, but those files are easy to open on their own. Do not insert a markdown banner into a data file. A short `UNPUBLISHED.md` (or equivalent) in each of those folders, and beside the dictionary CSV, would close the gap without corrupting the data.

- **Hit if:** Those branch-only data trees still have no unpublished-vs-`main` notice in the folder that contains them.
- **Miss if:** Each such folder already has a clear unpublished-vs-`main` notice, or the claim already excluded binary/data files and said the parent writeup was sufficient.
