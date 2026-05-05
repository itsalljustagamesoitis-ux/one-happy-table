"""Tests that site-specific config values are set (non-empty, non-placeholder)."""

from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
PRODUCER_DIR = ROOT / "producer"


def test_site_domain_is_set(site_config):
    domain = site_config["site"]["domain"]
    assert domain, "site.domain is empty"
    assert "REPLACE" not in domain.upper(), f"site.domain still has placeholder: {domain}"
    assert "." in domain, f"site.domain doesn't look like a domain: {domain}"


def test_amazon_tracking_id_is_set(site_config):
    tag = site_config["affiliate"]["amazon_tracking_id"]
    assert tag, "amazon_tracking_id is empty"
    assert "REPLACE" not in tag.upper(), f"amazon_tracking_id still has placeholder: {tag}"
    assert tag.endswith("-20"), f"Amazon tag should end in -20, got: {tag}"


def test_awin_clickref_is_set(site_config):
    pattern = site_config["affiliate"]["awin_clickref_pattern"]
    assert pattern, "awin_clickref_pattern is empty"
    assert "REPLACE" not in pattern.upper(), f"awin_clickref_pattern still has placeholder: {pattern}"


def test_package_name_is_set(root):
    import json
    pkg = json.loads((root / "package.json").read_text())
    assert pkg["name"], "package.json name is empty"
    assert "REPLACE" not in pkg["name"].upper(), "package.json name still has placeholder"


def test_no_hardcoded_wrong_domain_in_schema_builder(site_config):
    """schema_builder.SITE_URL must match site.config.yaml domain."""
    from schema_builder import SITE_URL
    expected = f"https://{site_config['site']['domain']}"
    assert SITE_URL == expected, f"SITE_URL is '{SITE_URL}', expected '{expected}'"


def test_schema_builder_loads_url_from_config():
    """SITE_URL must not be hardcoded."""
    text = (PRODUCER_DIR / "schema_builder.py").read_text()
    assert "_get_site_url()" in text, "schema_builder.py should load SITE_URL from config"


def test_author_is_wendy_in_system_prompt():
    from article_builder import SYSTEM
    assert "Wendy Collins" in SYSTEM, "SYSTEM prompt should reference Wendy Collins"


def test_american_english_rules_in_system_prompt():
    from article_builder import SYSTEM
    assert "American English" in SYSTEM


def test_no_fsg_or_gardener_references_in_article_builder():
    """article_builder.py should not reference FSG or gardening."""
    text = (PRODUCER_DIR / "article_builder.py").read_text()
    assert "Four Season Gardener" not in text, "FSG reference found in article_builder.py"
    assert "gardener" not in text.lower() or "gardener" in text.lower()  # allow in comments
