# djw1
This repository is a proof-of-concept testbed for a proposed architecture.
BDRC wants an audit tool and an asset manager platform. They share common components
One needs to be installed on local machines, one on master servers serving a wide community.
This repository is a test implementation which has
```
+-- |  root
    |
    +--  audit tool django site
    | + templates
    | + views
    | + migrations
    | + sqlite.db
    |
    +-- Asset Manager django site
    | + templates
    | + views
    | + migrations
    | + MySQL db
    |
    + ---- bdrclib
    | + Models
    | + supporting classes
    | + Other data structures
```
The test is to see if we can build pip or other installation media for each django site.
Ideally, bdrclib could be auto-included in each package, so it wouldn't have to be listed as a separate pre-requisite,
but even if it were, that would be ok.
