"""Tests for pipeline.json structural integrity."""

import pytest
from collections import Counter

VALID_TYPES = {
    "roundup", "review", "comparison", "informational", "buyer_guide",
    "Roundup", "Review", "Comparison", "Informational", "Buyer Guide",
}


class TestPipelineStructure:
    def test_pipeline_is_non_empty(self, pipeline):
        assert len(pipeline) > 0, "pipeline.json is empty"

    def test_all_articles_have_required_fields(self, pipeline):
        required = ["id", "slug", "keyword", "type", "hub"]
        bad = []
        for a in pipeline:
            missing = [f for f in required if not a.get(f)]
            if missing:
                bad.append(f"id={a.get('id','?')}: missing {missing}")
        assert not bad, f"{len(bad)} articles missing required fields:\n" + "\n".join(bad[:10])

    def test_no_duplicate_ids(self, pipeline):
        ids = [a["id"] for a in pipeline]
        dupes = [id_ for id_, count in Counter(ids).items() if count > 1]
        assert not dupes, f"Duplicate article IDs: {dupes}"

    def test_no_duplicate_slugs(self, pipeline):
        slugs = [a["slug"] for a in pipeline]
        dupes = [s for s, count in Counter(slugs).items() if count > 1]
        assert not dupes, f"Duplicate slugs: {dupes}"

    def test_all_types_are_valid(self, pipeline):
        bad = [f"id={a['id']} slug={a['slug']}: type='{a.get('type')}'"
               for a in pipeline if a.get("type") not in VALID_TYPES]
        assert not bad, f"Invalid article types:\n" + "\n".join(bad[:10])

    def test_all_hubs_exist_in_navigation(self, pipeline, all_hub_slugs):
        bad = []
        for a in pipeline:
            hub = a.get("hub_slug") or a.get("hub", "")
            if hub not in all_hub_slugs:
                bad.append(f"id={a['id']} slug={a['slug']}: hub='{hub}'")
        assert not bad, f"{len(bad)} articles reference hubs not in navigation.yaml:\n" + "\n".join(bad[:10])


class TestProductsCatalog:
    def test_catalog_loads(self, products):
        assert len(products) > 0, "products.yaml is empty"

    def test_all_products_have_required_fields(self, products):
        required = ["name", "brand", "price_band", "default_pros", "default_cons"]
        bad = []
        for key, p in products.items():
            missing = [f for f in required if not p.get(f)]
            if "amazon_asin" not in p:
                missing.append("amazon_asin (key missing)")
            if missing:
                bad.append(f"'{key}': missing {missing}")
        assert not bad, f"{len(bad)} products missing required fields:\n" + "\n".join(bad[:10])


class TestGeneratedArticles:
    def _load_articles(self, root):
        import yaml
        articles = []
        for md_file in (root / "content/articles").glob("*.md"):
            text = md_file.read_text()
            if not text.startswith("---"):
                continue
            parts = text.split("---", 2)
            if len(parts) < 3:
                continue
            try:
                data = yaml.safe_load(parts[1])
                data["_file"] = md_file.name
                articles.append(data)
            except Exception:
                pass
        return articles

    def test_no_slug_based_hero_images(self, root):
        articles = self._load_articles(root)
        bad = [f"{a['_file']}: {a.get('hero_image')}" for a in articles if "-hero.jpg" in a.get("hero_image", "")]
        assert not bad, f"Articles using slug-based hero images: {bad}"

    def test_hero_images_exist_on_disk(self, root):
        articles = self._load_articles(root)
        image_dir = root / "public/images/articles"
        bad = []
        for a in articles:
            img = a.get("hero_image", "").replace("articles/", "")
            if img and not (image_dir / img).exists():
                bad.append(f"{a['_file']}: {img}")
        assert not bad, f"Hero image files missing:\n" + "\n".join(bad)

    def test_author_field_is_set(self, root):
        articles = self._load_articles(root)
        bad = [a["_file"] for a in articles if not a.get("author")]
        assert not bad, f"Articles with missing author field: {bad}"
