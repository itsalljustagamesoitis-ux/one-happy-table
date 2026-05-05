"""Tests for data_loader.py — enrich_article, get_hub_products, get_pending_articles."""

import pytest
from data_loader import enrich_article, get_hub_products, get_pending_articles


class TestEnrichArticle:
    def test_populates_hub_label(self, navigation):
        article = {"hub": "dinnerware"}
        enrich_article(article, navigation)
        assert article["hub_label"] == "Dinnerware & China"

    def test_populates_hub_url(self, navigation):
        article = {"hub": "glassware"}
        enrich_article(article, navigation)
        assert article["hub_url"] == "/glassware/"

    def test_populates_hub_slug(self, navigation):
        article = {"hub": "linens"}
        enrich_article(article, navigation)
        assert article["hub_slug"] == "linens"

    def test_populates_category_label(self, navigation):
        article = {"hub": "dinnerware"}
        enrich_article(article, navigation)
        assert article["category_label"] == "Home Entertaining"

    def test_populates_category_slug(self, navigation):
        article = {"hub": "serveware"}
        enrich_article(article, navigation)
        assert article["category_slug"] == "home-entertaining"

    def test_all_hubs_resolve_category(self, navigation, all_hub_slugs):
        for hub_slug in all_hub_slugs:
            article = {"hub": hub_slug}
            enrich_article(article, navigation)
            assert article.get("category_label"), f"Hub '{hub_slug}' produced empty category_label"
            assert article.get("category_slug"), f"Hub '{hub_slug}' produced empty category_slug"

    def test_unknown_hub_gets_fallback(self, navigation):
        article = {"hub": "nonexistent-hub"}
        enrich_article(article, navigation)
        assert article["hub_slug"] == "nonexistent-hub"
        assert article["hub_url"] == "/nonexistent-hub/"
        assert article["category_label"] == ""

    def test_does_not_overwrite_existing_hub_label(self, navigation):
        article = {"hub": "dinnerware", "hub_label": "Already Set"}
        enrich_article(article, navigation)
        assert article["hub_label"] == "Dinnerware & China"


class TestGetHubProducts:
    def test_returns_only_matching_hub(self, products):
        result = get_hub_products(products, "dinnerware")
        for key, p in result.items():
            assert p.get("category") == "dinnerware" or p.get("hub") == "dinnerware", \
                f"Product '{key}' does not belong to dinnerware"

    def test_excludes_other_hubs(self, products):
        dinnerware = get_hub_products(products, "dinnerware")
        glassware = get_hub_products(products, "glassware")
        overlap = set(dinnerware.keys()) & set(glassware.keys())
        assert not overlap, f"Products appear in both dinnerware and glassware: {overlap}"

    def test_returns_empty_for_unknown_hub(self, products):
        result = get_hub_products(products, "nonexistent")
        assert result == {}


class TestGetPendingArticles:
    def test_excludes_published_articles(self, pipeline):
        pending = get_pending_articles(pipeline)
        for a in pending:
            assert not a.get("published", False), f"Article {a['id']} is published but appeared in pending"

    def test_includes_unpublished_articles(self, pipeline):
        pending = get_pending_articles(pipeline)
        unpublished_count = sum(1 for a in pipeline if not a.get("published", False))
        assert len(pending) == unpublished_count
