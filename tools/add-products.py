#!/usr/bin/env python3
"""
add-products.py — Appends 85 new catalog entries to OHT products.yaml.
Run once. Atomic write (tmp → bak → final).
"""

import yaml, os, shutil

PRODUCTS_PATH = os.path.join(os.path.dirname(__file__), '..', 'content', 'products', 'products.yaml')
PRODUCTS_PATH = os.path.normpath(PRODUCTS_PATH)

NOTE = "added manually, catalog-growth session 2026-05-05"

NEW_PRODUCTS = {

    # ── Dinnerware: Charger Plates ────────────────────────────────────────────

    "american-atelier-black-gold-charger-set4": {
        "name": "American Atelier Black and Gold Charger Plates Set of 4",
        "brand": "American Atelier",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Black rim with gold border elevates any place setting without dominating the dinnerware",
            "Plastic construction makes them unbreakable for outdoor or catered events",
        ],
        "default_cons": [
            "Lightweight plastic feel is apparent up close — not suitable for formal seated dinners",
        ],
        "notes_for_writers": NOTE,
    },

    "efavormart-clear-acrylic-charger-plates-set12": {
        "name": "Clear Acrylic Charger Plates with Gold Rim Set of 12",
        "brand": "Efavormart",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Clear body lets the table linens show through — works with any colour scheme",
            "12-pack makes them cost-effective for large dinner parties",
        ],
        "default_cons": [
            "Acrylic scratches over multiple uses — not a long-term investment piece",
        ],
        "notes_for_writers": NOTE,
    },

    "godinger-silver-charger-plates-set4": {
        "name": "Godinger Silver-Finish Round Charger Plates Set of 4",
        "brand": "Godinger",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Silver-tone finish photographs as polished pewter or mirror — versatile anchor for formal and casual tables",
            "Lightweight metal construction — lighter than glass chargers of the same look",
        ],
        "default_cons": [
            "Finish can tarnish over time with hand-washing; wipe dry immediately",
        ],
        "notes_for_writers": NOTE,
    },

    "mikasa-metropolitan-charger-plate": {
        "name": "Mikasa Metropolitan Charger Plate",
        "brand": "Mikasa",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Glazed porcelain edge holds its finish through regular dishwasher cycles",
            "Metropolitan line coordinates cleanly with Mikasa's bone china place settings",
        ],
        "default_cons": [
            "Sold individually rather than in sets — stocking a full table of 8 requires separate orders",
        ],
        "notes_for_writers": NOTE,
    },

    "lenox-opal-innocence-charger-plate": {
        "name": "Lenox Opal Innocence White Charger Plate",
        "brand": "Lenox",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Platinum-banded edge reads as elegant without requiring matching china in the same pattern",
            "Pairs seamlessly with the Opal Innocence 12-piece dinnerware set for a unified formal table",
        ],
        "default_cons": [
            "Platinum band is not dishwasher safe — hand-wash only to preserve the rim",
        ],
        "notes_for_writers": NOTE,
    },

    "juliska-berry-thread-charger-plate": {
        "name": "Juliska Berry & Thread Charger Plate",
        "brand": "Juliska",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Hand-crafted whitewash stoneware with hand-applied berry and thread motif — no two are identical",
            "The 13-inch rim is wide enough to act as a decorative centrepiece even before the first course",
        ],
        "default_cons": [
            "Premium price means a full table of 8 is a significant investment",
            "Hand-wash recommended to preserve the hand-painted relief",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Dinnerware: Bone China & Fine China ──────────────────────────────────

    "corelle-impressions-16pc-dinnerware": {
        "name": "Corelle Impressions 16-Piece Dinnerware Set",
        "brand": "Corelle",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Triple-layer Vitrelle glass is non-porous and chip-resistant — safer than glazed ceramics for lead/cadmium concerns",
            "Lightweight for a 16-piece set — noticeably easier to carry a full stack",
        ],
        "default_cons": [
            "Glass construction means it shatters rather than chipping when dropped — not truly unbreakable",
        ],
        "notes_for_writers": NOTE,
    },

    "churchill-willow-blue-4pc-place-setting": {
        "name": "Churchill Willow Blue 4-Piece Place Setting",
        "brand": "Churchill China",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Classic Willow blue-and-white pattern is produced continuously since the 1790s — a genuine heritage piece at an accessible price",
            "British bone china fired to commercial hospitality standards — more durable than domestic bone china at the same price",
        ],
        "default_cons": [
            "Traditional blue-and-white pattern is polarising — works for a collected, layered table aesthetic; looks out of place on minimalist tables",
        ],
        "notes_for_writers": NOTE,
    },

    "spode-blue-italian-5pc-place-setting": {
        "name": "Spode Blue Italian 5-Piece Place Setting",
        "brand": "Spode",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Blue Italian pattern has been in continuous production since 1816 — the most referenced pattern in comparative bone china articles",
            "Dishwasher safe despite the transfer print — Spode uses an underglaze process that survives repeated cycles",
        ],
        "default_cons": [
            "The Italianate landscape scene is a strong visual statement — harder to mix with other patterned pieces",
        ],
        "notes_for_writers": NOTE,
    },

    "portmeirion-botanic-garden-4pc-set": {
        "name": "Portmeirion Botanic Garden 4-Piece Dinnerware Set",
        "brand": "Portmeirion",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Each piece carries a different botanical illustration — inherently collectable and mix-and-match friendly",
            "Earthenware is dishwasher and microwave safe; practical for daily use despite the decorative surface",
        ],
        "default_cons": [
            "Earthenware chips more readily than stoneware or porcelain — the illustrated surfaces show chips prominently",
        ],
        "notes_for_writers": NOTE,
    },

    "noritake-colorwave-granite-4pc": {
        "name": "Noritake Colorwave Granite 4-Piece Place Setting",
        "brand": "Noritake",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Reactive-glaze finish in granite gives each piece a handmade stone texture at machine-fired consistency",
            "Stoneware construction is heavier and more chip-resistant than bone china at the same price tier",
        ],
        "default_cons": [
            "Granite colourway is a committed aesthetic — does not mix cleanly with white or patterned china",
        ],
        "notes_for_writers": NOTE,
    },

    "denby-halo-4pc-place-setting": {
        "name": "Denby Halo 4-Piece Place Setting",
        "brand": "Denby",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-crafted in Derbyshire, England — one of the few remaining UK stoneware producers still firing in their original factory",
            "The cream interior and dark blue exterior means different visual weight front and back — interesting on a stacked table",
        ],
        "default_cons": [
            "Denby stoneware is denser than most competitors; the 4-piece is noticeably heavier to carry and store",
        ],
        "notes_for_writers": NOTE,
    },

    "royal-worcester-evesham-gold-4pc": {
        "name": "Royal Worcester Evesham Gold 4-Piece Place Setting",
        "brand": "Royal Worcester",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Evesham Gold is one of the most collected Royal Worcester patterns — strong secondary market for individual pieces",
            "Fine English bone china with gold-lustre rim; the fruit-and-vine decoration is hand-applied on some archive pieces",
        ],
        "default_cons": [
            "Gold rim is not dishwasher safe — a commitment to hand-washing for a daily-use set",
        ],
        "notes_for_writers": NOTE,
    },

    "wedgwood-wild-strawberry-5pc": {
        "name": "Wedgwood Wild Strawberry 5-Piece Place Setting",
        "brand": "Wedgwood",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Wild Strawberry has been in continuous Wedgwood production since 1965 — the definitive mid-century English botanical tableware",
            "Bone china body is translucent when held to the light — the visual marker of true fine bone china",
        ],
        "default_cons": [
            "Hand-wash only; the pink-and-green botanical colour palette fades in the dishwasher over time",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Dinnerware: General Sets ──────────────────────────────────────────────

    "anchor-hocking-presence-glass-dinnerware": {
        "name": "Anchor Hocking Presence Glass Dinnerware Set",
        "brand": "Anchor Hocking",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Tempered glass construction is non-porous with zero lead or cadmium risk — the definitive non-toxic dinnerware choice",
            "Clear glass body shows the food, not the plate — works with any table colour scheme",
        ],
        "default_cons": [
            "Tempered glass shatters completely if dropped — no chipping, just full breakage",
        ],
        "notes_for_writers": NOTE,
    },

    "maison-arts-art-deco-dinnerware-16pc": {
        "name": "Maison Arts Art Deco Matte Black and Gold 16-Piece Dinnerware Set",
        "brand": "Maison Arts",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Matte black porcelain with gold rim is the most-photographed Art Deco dinnerware aesthetic on Pinterest",
            "16-piece serves 4 — practical for couples who entertain small dinner parties",
        ],
        "default_cons": [
            "Matte black shows dried water spots prominently — hand-dry immediately after washing",
        ],
        "notes_for_writers": NOTE,
    },

    "certified-intl-talavera-4pc-place-setting": {
        "name": "Certified International Talavera 4-Piece Place Setting",
        "brand": "Certified International",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-painted cobalt and terracotta Talavera design is authentic to the Mexican folk art tradition",
            "Stoneware construction is dishwasher safe despite the decorative surface",
        ],
        "default_cons": [
            "Strong pattern limits mixing — works best as a standalone set rather than layered with other china",
        ],
        "notes_for_writers": NOTE,
    },

    "gibson-elite-coastal-12pc-dinnerware": {
        "name": "Gibson Elite Coastal Series 12-Piece Dinnerware Set",
        "brand": "Gibson",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Serves 4 in a 12-piece set — a practical starter set for couples moving to a formal table",
            "Stoneware construction is more durable than porcelain at the same budget price point",
        ],
        "default_cons": [
            "Coastal motifs are seasonal in feel — less flexible for year-round formal entertaining",
        ],
        "notes_for_writers": NOTE,
    },

    "lenox-opal-innocence-12pc-set": {
        "name": "Lenox Opal Innocence 12-Piece Dinnerware Set",
        "brand": "Lenox",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Serves 4 in bone china with platinum band — the benchmark for American fine dining china at mid-premium price",
            "Full Opal Innocence line allows expansion: add charger plates, serving pieces, and mugs in the same pattern",
        ],
        "default_cons": [
            "Platinum band is hand-wash only — a consideration for households that rely heavily on the dishwasher",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Dinnerware: Mugs & Cups ───────────────────────────────────────────────

    "royal-doulton-gordon-ramsay-maze-mug": {
        "name": "Royal Doulton Gordon Ramsay Maze White Mug",
        "brand": "Royal Doulton",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Fine bone china construction is noticeably lighter and more translucent than stoneware mugs at the same price",
            "Coordinates with the Gordon Ramsay Maze 4-piece place setting already in the catalog",
        ],
        "default_cons": [
            "Fine bone china chips at the rim more readily than stoneware — not ideal for a household with children",
        ],
        "notes_for_writers": NOTE,
    },

    "portmeirion-botanic-garden-mug": {
        "name": "Portmeirion Botanic Garden 10-Ounce Mug",
        "brand": "Portmeirion",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Each mug carries a different botanical illustration — buying a set creates instant variety without pattern repetition",
            "Earthenware is microwave and dishwasher safe; the botanical illustrations survive repeated cycles",
        ],
        "default_cons": [
            "10-ounce capacity is smaller than a standard American coffee mug — may feel insufficient for large morning drinks",
        ],
        "notes_for_writers": NOTE,
    },

    "wedgwood-vera-wang-lace-teacup-saucer": {
        "name": "Wedgwood Vera Wang Lace Bone China Teacup and Saucer",
        "brand": "Wedgwood",
        "hub": "dinnerware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Vera Wang lace-embossed bone china is the most recognised teacup design for formal afternoon tea settings",
            "Platinum-trimmed saucer doubles as an individual dessert plate for petit fours",
        ],
        "default_cons": [
            "Platinum trim requires hand-washing — not suitable for daily use in households reliant on the dishwasher",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Glassware: Champagne Flutes ───────────────────────────────────────────

    "libbey-embassy-champagne-flutes-set8": {
        "name": "Libbey Embassy Champagne Flutes Set of 8",
        "brand": "Libbey",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "8-pack at a budget price makes them practical for parties where breakage is expected",
            "Made in the USA with Safedge rim guarantee — unusually durable for a budget flute",
        ],
        "default_cons": [
            "Machine-pressed glass lacks the clarity of mouth-blown crystal — visible seam lines under close inspection",
        ],
        "notes_for_writers": NOTE,
    },

    "govino-champagne-flutes-set4": {
        "name": "Govino Shatterproof Flexible Champagne Flutes Set of 4",
        "brand": "Govino",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "BPA-free flexible polymer is genuinely shatterproof — the only flute safe for outdoor venues and poolside",
            "Thumb notch on the base is a patented ergonomic detail that prevents smudging the bowl",
        ],
        "default_cons": [
            "Polymer walls retain a slight flex that is visually apparent — not suitable when crystal clarity is expected",
        ],
        "notes_for_writers": NOTE,
    },

    "estelle-colored-glass-champagne-cobalt-set2": {
        "name": "Estelle Colored Glass Champagne Flutes Cobalt Blue Set of 2",
        "brand": "Estelle Colored Glass",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-blown cobalt glass is the leading coloured-champagne-flute aesthetic in interior design editorial",
            "The coloured stem catches candlelight — a decorative piece as much as a functional one",
        ],
        "default_cons": [
            "Sold in pairs — a table of 8 requires four orders at significant cumulative cost",
        ],
        "notes_for_writers": NOTE,
    },

    "luigi-bormioli-atelier-champagne-set6": {
        "name": "Luigi Bormioli Atelier Champagne Flutes Set of 6",
        "brand": "Luigi Bormioli",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Titanium-reinforced glass resists breakage at the stem — the engineering advantage Luigi Bormioli is known for",
            "Sold in a 6-pack — practical for a dinner party without additional orders",
        ],
        "default_cons": [
            "Titanium reinforcement slightly reduces clarity versus mouth-blown crystal — not detectable in use, visible side-by-side",
        ],
        "notes_for_writers": NOTE,
    },

    "riedel-veloce-champagne-glass-set2": {
        "name": "Riedel Veloce Champagne Wine Glass Set of 2",
        "brand": "Riedel",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Veloce is Riedel's machine-blown lead-free crystal line — crystal clarity at significantly lower price than hand-blown",
            "The Champagne Wine format is wider than a standard flute — champagne experts favour the wider bowl for aroma expression",
        ],
        "default_cons": [
            "Dishwasher safe but the machine-blown seam is faintly visible at the base of the bowl",
        ],
        "notes_for_writers": NOTE,
    },

    "zwiesel-glas-enoteca-champagne-set2": {
        "name": "Zwiesel Glas Enoteca Champagne Flute Set of 2",
        "brand": "Zwiesel Glas",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Tritan crystal is dishwasher safe without the cloudiness that afflicts standard lead-free crystal over time",
            "Long, fine stem is the defining visual of the Enoteca line — the premium design reference for champagne flute comparisons",
        ],
        "default_cons": [
            "Tall stem increases breakage risk at the base point — hand-carry rather than dishwasher-load standing upright",
        ],
        "notes_for_writers": NOTE,
    },

    "waterford-millennium-champagne-flutes-set2": {
        "name": "Waterford Millennium Series Champagne Flutes Set of 2",
        "brand": "Waterford",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Millennium Series is Waterford's most-gifted champagne flute — the reference product for the waterford-crystal-millennium-champagne-flutes keyword",
            "Full lead-free crystal with Waterford's signature deep-cut geometric facets",
        ],
        "default_cons": [
            "Hand-wash only to maintain the cut-crystal brilliance — dishwasher dulls the facets permanently",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Glassware: Wine Glasses ───────────────────────────────────────────────

    "bormioli-rocco-bistro-wine-glasses-set6": {
        "name": "Bormioli Rocco Bistro Wine Glasses Set of 6",
        "brand": "Bormioli Rocco",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Italian-made tempered glass at budget pricing — the standard reference for bistro-style wine service",
            "Sold in a 6-pack with a foot-to-rim height that photographs as a full bistro table setup",
        ],
        "default_cons": [
            "Tempered glass is thicker than crystal — the rim diameter is slightly wider than a fine wine glass, which affects the pour",
        ],
        "notes_for_writers": NOTE,
    },

    "libbey-paneled-ribbed-wine-glasses-set4": {
        "name": "Libbey Signature Paneled Ribbed Wine Glasses Set of 4",
        "brand": "Libbey",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Vertical panel ribbing provides grip and a textural contrast to plain crystal on the same table",
            "Made in the USA with Safedge rim guarantee — budget price, above-budget durability",
        ],
        "default_cons": [
            "Ribbing collects calcium deposits in hard-water areas — requires a white vinegar rinse periodically",
        ],
        "notes_for_writers": NOTE,
    },

    "estelle-colored-glass-wine-emerald-set6": {
        "name": "Estelle Colored Glass Wine Glasses Emerald Green Set of 6",
        "brand": "Estelle Colored Glass",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-blown emerald glass is the leading coloured wine glass in current interior design editorial — the reference product for green-wine-glasses articles",
            "Sold as a set of 6 — practical for a dinner party without multiple orders",
        ],
        "default_cons": [
            "Colour intensity varies between hand-blown pieces — minor inconsistency is part of the craft, but visible side by side",
        ],
        "notes_for_writers": NOTE,
    },

    "simon-pearce-ascutney-red-wine-glass": {
        "name": "Simon Pearce Ascutney Red Wine Glass",
        "brand": "Simon Pearce",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Mouth-blown in Vermont — each glass has a subtle organic irregularity that distinguishes it from machine production",
            "Thick base and generous bowl make it the most stable of Simon Pearce's wine glasses for a set table",
        ],
        "default_cons": [
            "Hand-blown glass requires hand-washing — premium care for a premium piece",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Glassware: Decanters ──────────────────────────────────────────────────

    "anchor-hocking-glass-carafe-1.5l": {
        "name": "Anchor Hocking 1.5-Liter Glass Carafe with Lid",
        "brand": "Anchor Hocking",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "The reference product for decanter-vs-carafe comparisons — carafe design is explicitly for still water and juice, not wine",
            "Dishwasher safe and inexpensive — practical for everyday table water service",
        ],
        "default_cons": [
            "No pouring collar — the wide mouth drips slightly on the pour stroke",
        ],
        "notes_for_writers": NOTE,
    },

    "ravenscroft-crystal-whiskey-decanter": {
        "name": "Ravenscroft Crystal Taylor Whiskey Decanter",
        "brand": "Ravenscroft Crystal",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Lead-free crystal with a wide base designed for spirit storage — the mid-range reference for whiskey decanter comparisons",
            "Polished flat-cut pattern is formal without being ornate",
        ],
        "default_cons": [
            "Crystal stopper requires hand-drying immediately — calcium deposits around the stopper collar are hard to remove",
        ],
        "notes_for_writers": NOTE,
    },

    "riedel-corneto-decanter": {
        "name": "Riedel Corneto Decanter",
        "brand": "Riedel",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Conical form forces wine against the widest surface area of the glass — more efficient aeration than flat-bottomed decanters",
            "Riedel's machine-blown lead-free crystal at mid-market pricing",
        ],
        "default_cons": [
            "The cone form makes it difficult to dry completely without a decanter drying stand",
        ],
        "notes_for_writers": NOTE,
    },

    "waterford-lismore-crystal-decanter": {
        "name": "Waterford Lismore Crystal Whiskey Decanter",
        "brand": "Waterford",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Lismore pattern is Waterford's most recognised — the premium benchmark for whiskey decanter gift guides",
            "Deep diamond and wedge cuts on the body refract light across a room",
        ],
        "default_cons": [
            "Cut crystal stopper is not airtight for long-term spirit storage — best used for serving rather than ageing",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Glassware: Cocktail Glasses ───────────────────────────────────────────

    "libbey-midtown-stemless-cocktail-set12": {
        "name": "Libbey Midtown Stemless Cocktail Glasses Set of 12",
        "brand": "Libbey",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "12-pack makes them economical for home bars where breakage over time is the norm",
            "Stemless form reduces breakage risk versus stemmed cocktail glasses",
        ],
        "default_cons": [
            "Stemless means the hand warms the drink — not suitable for cocktails served at precise cold temperatures",
        ],
        "notes_for_writers": NOTE,
    },

    "schott-zwiesel-pure-coupe-glasses-set6": {
        "name": "Schott Zwiesel Pure Coupe Glasses Set of 6",
        "brand": "Schott Zwiesel",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Tritan crystal coupe is dishwasher safe — the key practical advantage over vintage coupe glass",
            "The wide, shallow bowl is the correct format for a sidecar, Daiquiri, or champagne coupe serve",
        ],
        "default_cons": [
            "Wide bowl means carbonation dissipates faster — not ideal for sparkling wine service despite the association",
        ],
        "notes_for_writers": NOTE,
    },

    "luigi-bormioli-optica-cocktail-set6": {
        "name": "Luigi Bormioli Optica Cocktail Glasses Set of 6",
        "brand": "Luigi Bormioli",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Tall Collins-style glass in titanium-reinforced crystal — practical for highball serves and iced cocktails",
            "Optica line is noted for exceptional clarity — visual reference for tall-cocktail-glass comparisons",
        ],
        "default_cons": [
            "Tall form makes these more prone to tipping than wide-base rocks glasses",
        ],
        "notes_for_writers": NOTE,
    },

    "riedel-bar-highball-glasses-set2": {
        "name": "Riedel Bar Drink Specific Highball Glasses Set of 2",
        "brand": "Riedel",
        "hub": "glassware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Riedel's Drink Specific series is designed for cocktail category — the highball form is engineered for G&T and Collins-style drinks",
            "Machine-blown lead-free crystal at mid-premium pricing for the Riedel name",
        ],
        "default_cons": [
            "Sold in pairs only — stocking a full bar kit requires multiple orders at premium cost",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Linens: Tablecloths ───────────────────────────────────────────────────

    "linen-tablecloth-black-rectangle-60x102": {
        "name": "LinenTablecloth Black Polyester Tablecloth 60x102",
        "brand": "LinenTablecloth",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Covers a standard 6-foot rectangular folding table to the floor — the most-needed size for a 60-x-102 tablecloth article",
            "Machine washable polyester — practical for repeated entertaining use",
        ],
        "default_cons": [
            "Polyester shows wrinkles from storage more than linen — requires steaming before a formal dinner",
        ],
        "notes_for_writers": NOTE,
    },

    "linen-tablecloth-navy-blue-90x132": {
        "name": "LinenTablecloth Navy Blue Tablecloth 90x132",
        "brand": "LinenTablecloth",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "90x132 inch size covers a 8-foot banquet table with a full drop — the reference size for 90-x-132-table-linens articles",
            "Navy blue is the most-searched tablecloth colour for formal dining and holiday tables",
        ],
        "default_cons": [
            "Deep navy shows lint and pet hair prominently — a lint roller is essential before guests arrive",
        ],
        "notes_for_writers": NOTE,
    },

    "linen-tablecloth-green-gingham-check": {
        "name": "LinenTablecloth Green Gingham Check Tablecloth",
        "brand": "LinenTablecloth",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Classic green gingham is the standard reference for both gingham-cloth-tablecloth and green-plaid-tablecloth articles",
            "Woven check means the pattern is inherent to the fabric — not a print that fades after washing",
        ],
        "default_cons": [
            "Cotton-poly blend is less crisp than 100% cotton gingham and requires ironing to look sharp",
        ],
        "notes_for_writers": NOTE,
    },

    "maison-hermine-red-velvet-tablecloth": {
        "name": "Maison d'Hermine Red Velvet Oblong Tablecloth",
        "brand": "Maison d'Hermine",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Velvet pile catches and scatters candlelight across the table surface — a dramatic effect at budget pricing",
            "Machine washable on delicate cycle — more practical than it looks",
        ],
        "default_cons": [
            "Velvet pile is directional — brushing the wrong way leaves visible marks that require re-smoothing",
        ],
        "notes_for_writers": NOTE,
    },

    "april-cornell-pomegranate-tablecloth": {
        "name": "April Cornell Pomegranate Tablecloth",
        "brand": "April Cornell",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "April Cornell's pomegranate print is a rich jewel-tone pattern that anchors autumn and winter tablescapes",
            "100% cotton construction drapes naturally without the stiffness of linen blends",
        ],
        "default_cons": [
            "Deep colours require cold-water washing to prevent running — not a tablecloth for a rushed post-dinner cleanup",
        ],
        "notes_for_writers": NOTE,
    },

    "april-cornell-floral-linen-tablecloth": {
        "name": "April Cornell Vintage Floral Linen Tablecloth",
        "brand": "April Cornell",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "April Cornell's signature vintage-botanical print coordinates naturally with mixed antique china — the brand's core aesthetic",
            "Available in multiple sizes to fit round and oval tables",
        ],
        "default_cons": [
            "Floral print is a strong visual commitment — works for a collected, layered table, not minimalist settings",
        ],
        "notes_for_writers": NOTE,
    },

    "waterford-stewart-plaid-tartan-tablecloth": {
        "name": "Waterford Stewart Plaid Tartan Tablecloth",
        "brand": "Waterford",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Stewart Plaid is one of Scotland's most recognised clan tartans — a historically authentic pattern for tartan-plaid-tablecloth articles",
            "Waterford's linens license produces hotel-quality fabric weight — noticeably heavier than budget tartan polyester",
        ],
        "default_cons": [
            "Dry-clean recommended to maintain the fabric weight and colour — limits spontaneous post-dinner laundering",
        ],
        "notes_for_writers": NOTE,
    },

    "juliska-country-estate-tablecloth": {
        "name": "Juliska Country Estate Tablecloth",
        "brand": "Juliska",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Country Estate pattern coordinates directly with Juliska's ceramic dinnerware line — a unified table for collectors",
            "Stonewashed linen has a relaxed, lived-in drape that suits the Country Estate farmhouse aesthetic",
        ],
        "default_cons": [
            "Linen wrinkles are part of the design intent — not suitable for guests who expect a pressed formal cloth",
        ],
        "notes_for_writers": NOTE,
    },

    "sferra-festival-ivory-tablecloth": {
        "name": "Sferra Festival Ivory Tablecloth",
        "brand": "Sferra",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "100% Egyptian cotton in ivory — the neutral anchor for a formal table that works with any china pattern",
            "Festival's tight woven construction drapes without bulk and holds a pressed crease all evening",
        ],
        "default_cons": [
            "Cotton requires careful ironing to achieve the formal pressed finish Sferra is known for",
        ],
        "notes_for_writers": NOTE,
    },

    "sferra-classico-hemstitched-tablecloth": {
        "name": "Sferra Classico Hemstitched Tablecloth",
        "brand": "Sferra",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Hand-drawn hemstitch border is executed by artisans — the detail that distinguishes Classico from machine-hemmed alternatives",
            "Italian linen construction has the crisp drape and slight sheen that holds candlelight better than cotton",
        ],
        "default_cons": [
            "Premium linen requires hand-wash or gentle machine wash and professional pressing — significant care commitment",
        ],
        "notes_for_writers": NOTE,
    },

    "peacock-alley-hemstitch-tablecloth": {
        "name": "Peacock Alley Hemstitch Tablecloth",
        "brand": "Peacock Alley",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "American-made with Egyptian-cotton yarns — the premium domestic alternative to Italian linen for hemstitched tablecloths",
            "Available in dusty blue and other muted tones that are difficult to find in hemstitched linen at any price",
        ],
        "default_cons": [
            "Premium price and limited retail availability make replacement of individual pieces difficult",
        ],
        "notes_for_writers": NOTE,
    },

    "yves-delorme-triomphe-tablecloth": {
        "name": "Yves Delorme Triomphe Tablecloth",
        "brand": "Yves Delorme",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "French-made damask linen with a self-pattern that reads as textured under candlelight — the benchmark for luxury tablecloths in editorial",
            "Triomphe is Yves Delorme's signature line — available in gold and other formal colourways that are rare in the premium tier",
        ],
        "default_cons": [
            "Dry-clean only; at this price point that is an expected cost of ownership",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Linens: Table Runners ─────────────────────────────────────────────────

    "linen-tablecloth-black-white-check-runner": {
        "name": "LinenTablecloth Black and White Check Table Runner",
        "brand": "LinenTablecloth",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Black-and-white check is the most graphic, versatile runner pattern — works over a white, ivory, or bare wood table",
            "Machine washable — practical for weekly entertaining use",
        ],
        "default_cons": [
            "Woven check pattern can shift alignment after washing — re-press on the bias to restore the pattern",
        ],
        "notes_for_writers": NOTE,
    },

    "dii-sarape-striped-table-runner": {
        "name": "DII Sarape Striped Table Runner",
        "brand": "DII",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Authentic sarape stripe pattern in traditional Mexican colours — the reference product for sarape-table-runners and mexican-table-runners articles",
            "Machine washable and colourfast at low temperature",
        ],
        "default_cons": [
            "Cotton weave is lighter than premium table runners — may shift on a smooth table without a non-slip pad",
        ],
        "notes_for_writers": NOTE,
    },

    "chilewich-trellis-woven-navy-runner": {
        "name": "Chilewich Trellis Woven Table Runner in Navy",
        "brand": "Chilewich",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Chilewich's vinyl-yarn weave is heat-resistant, water-resistant, and machine washable — fundamentally more durable than linen runners",
            "Navy Trellis is their most-photographed colourway for formal dining editorial",
        ],
        "default_cons": [
            "The vinyl-yarn construction has a slight sheen and texture that reads as modern rather than traditional",
        ],
        "notes_for_writers": NOTE,
    },

    "juliska-country-estate-table-runner": {
        "name": "Juliska Country Estate Table Runner",
        "brand": "Juliska",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Country Estate linen runner coordinates with the full Juliska ceramic and linen table collection",
            "Stonewashed finish means it does not require ironing — intentionally relaxed for a farmhouse aesthetic",
        ],
        "default_cons": [
            "Premium pricing for a runner that explicitly does not press flat — a judgement call on the value of the brand's aesthetic",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Linens: Napkin Rings ──────────────────────────────────────────────────

    "wallace-silversmith-napkin-rings-set4": {
        "name": "Wallace Silversmiths Antique Silverplate Napkin Rings Set of 4",
        "brand": "Wallace Silversmiths",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Silverplate construction gives an antique sterling appearance at a fraction of the cost",
            "Wallace is a historic American silver brand — adds provenance to the antique-sterling-silver-napkin-rings article narrative",
        ],
        "default_cons": [
            "Silverplate tarnishes faster than solid sterling — requires periodic polishing",
        ],
        "notes_for_writers": NOTE,
    },

    "creative-co-op-bow-napkin-rings-set6": {
        "name": "Creative Co-Op Bow Linen Fabric Napkin Rings Set of 6",
        "brand": "Creative Co-Op",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Fabric bow form is the only napkin ring style that matches the bow-candle-holder aesthetic for a unified table theme",
            "Soft construction means no scratching on fine napkin fabric",
        ],
        "default_cons": [
            "Fabric rings absorb spills and require hand-washing — not as practical as metal rings for a busy household",
        ],
        "notes_for_writers": NOTE,
    },

    "michael-aram-anemone-napkin-ring-set4": {
        "name": "Michael Aram Anemone Napkin Ring Set of 4",
        "brand": "Michael Aram",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-crafted sculptural flower form in oxidised metal — the design aesthetic that defines Michael Aram's position in decorative napkin rings",
            "Anemone pattern coordinates with Michael Aram's flatware and serving pieces for a unified table",
        ],
        "default_cons": [
            "Three-dimensional petal construction catches on linen napkin fibres when sliding on — requires care to avoid snags",
        ],
        "notes_for_writers": NOTE,
    },

    "juliska-country-estate-napkin-ring": {
        "name": "Juliska Country Estate Napkin Ring",
        "brand": "Juliska",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Country Estate pattern coordinates directly with Juliska's ceramics, linens, and runners for a complete table collection",
            "Ceramic construction is more substantial than plated metal rings — sits steadily on the table",
        ],
        "default_cons": [
            "Ceramic is fragile; a dropped napkin ring chips at the edge — more fragile than metal alternatives",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Linens: Cloth Napkins ─────────────────────────────────────────────────

    "utopia-kitchen-cloth-napkins-green-set12": {
        "name": "Utopia Kitchen Cloth Dinner Napkins Green Set of 12",
        "brand": "Utopia Kitchen",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "12-pack at budget pricing makes cloth napkins genuinely cost-competitive with disposable paper napkins over a season",
            "Available in multiple colours including green and yellow — the reference for cloth-napkins-green and yellow-napkins-cloth articles",
        ],
        "default_cons": [
            "Cotton-poly blend pills slightly after repeated washing — not the texture of a restaurant-grade linen napkin",
        ],
        "notes_for_writers": NOTE,
    },

    "april-cornell-floral-cloth-napkins-set4": {
        "name": "April Cornell Garden Floral Cloth Napkins Set of 4",
        "brand": "April Cornell",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "April Cornell's botanical print coordinates with their tablecloths for a matched set",
            "100% cotton napkins absorb well and soften further with each wash",
        ],
        "default_cons": [
            "Sold in sets of 4 — a table of 8 requires two orders",
        ],
        "notes_for_writers": NOTE,
    },

    "sferra-hemstitched-linen-napkins-set4": {
        "name": "Sferra Hemstitched Linen Napkins Set of 4",
        "brand": "Sferra",
        "hub": "linens",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Hand-hemstitched border on Italian linen — the detail that distinguishes these from machine-finished napkins at any price",
            "Linen napkins improve with washing — the fibre softens and gains drape over time",
        ],
        "default_cons": [
            "Premium linen requires ironing after each wash to achieve the pressed formal finish",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Decor: Candle Holders ─────────────────────────────────────────────────

    "circleware-clear-glass-votive-set12": {
        "name": "Circleware Clear Glass Votive Candle Holders Set of 12",
        "brand": "Circleware",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "12-pack at budget pricing — enough to line a full dinner table with candlelight",
            "Clear glass is neutral — works with any coloured votive candle including red, which the red-candle-votive article targets",
        ],
        "default_cons": [
            "Thin glass walls scratch from metal tongs when removing spent candles",
        ],
        "notes_for_writers": NOTE,
    },

    "creative-co-op-bubble-glass-tealight-set4": {
        "name": "Creative Co-Op Bubble Glass Tealight Candle Holders Set of 4",
        "brand": "Creative Co-Op",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Bubble-textured glass wall scatters tealight glow across the table — the visual that defines bubble-glass-candle-holder articles",
            "Small footprint means they can be grouped in clusters or placed at each place setting",
        ],
        "default_cons": [
            "Bubble texture makes them difficult to clean fully if wax spills into the base",
        ],
        "notes_for_writers": NOTE,
    },

    "danya-b-metal-bow-candle-holders-pair": {
        "name": "Danya B. Metal Bow Taper Candle Holders Pair",
        "brand": "Danya B.",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Bow-shaped metal base is the specific design that the bow-candle-holder article targets",
            "Matte black or gold finish — coordinates with the black-and-gold charger plate aesthetic",
        ],
        "default_cons": [
            "Decorative form means the taper candle cup diameter may not accept all standard taper widths",
        ],
        "notes_for_writers": NOTE,
    },

    "michael-aram-twist-candle-holder": {
        "name": "Michael Aram Twist Candle Holder",
        "brand": "Michael Aram",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-crafted oxidised metal with the vine-twist motif that defines Michael Aram's sculptural aesthetic",
            "Covers the michael-aram-candle-holder article directly — the brand search that drives these queries",
        ],
        "default_cons": [
            "Three-dimensional form requires careful packing for storage to prevent bending the sculptural elements",
        ],
        "notes_for_writers": NOTE,
    },

    "nambe-copper-karim-rashid-candleholder": {
        "name": "Nambe Copper Candleholder by Karim Rashid",
        "brand": "Nambe",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Karim Rashid collaboration is the specific product named in the nambe-copper-centerpiece-karim-rashid article keyword",
            "Copper finish is warm and distinctive — contrasts with Nambe's typical alloy-metal aesthetic",
        ],
        "default_cons": [
            "Copper finish requires occasional polishing to prevent patina accumulation",
        ],
        "notes_for_writers": NOTE,
    },

    "white-porcelain-taper-candle-holders-set2": {
        "name": "White Porcelain Taper Candle Holders Set of 2",
        "brand": "Creative Co-Op",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "White porcelain is the canonical form for the porcelain-candle-holder article — coordinates with fine bone china on a formal table",
            "Cylindrical form accepts standard taper candle diameters without an adapter",
        ],
        "default_cons": [
            "Porcelain can crack if a taper burns down and the heat concentrates at the base",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Decor: Vases & Centerpiece Vessels ───────────────────────────────────

    "creative-co-op-bud-vases-set6": {
        "name": "Creative Co-Op White Ceramic Bud Vases Set of 6",
        "brand": "Creative Co-Op",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "6-pack in varying heights creates an instant clustered centerpiece without additional styling",
            "White ceramic is neutral and coordinates with all china and linen combinations",
        ],
        "default_cons": [
            "Narrow necks limit the stem diameter of flowers that fit — works best with single-stem or fine-stemmed flowers",
        ],
        "notes_for_writers": NOTE,
    },

    "libbey-glass-serving-bowl-set3": {
        "name": "Libbey Glass Serving Bowl Set of 3",
        "brand": "Libbey",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Nesting set of 3 provides multiple size options for glass-bowl-centerpiece and centerpiece-bowls-for-decoration articles",
            "Clear glass reads as both casual (fruit bowl) and formal (flower arrangement base)",
        ],
        "default_cons": [
            "Machine-pressed glass is visibly thicker than mouth-blown crystal of the same diameter",
        ],
        "notes_for_writers": NOTE,
    },

    "creative-co-op-whitewash-centerpiece-box": {
        "name": "Creative Co-Op Whitewash Wood Centerpiece Box with Handles",
        "brand": "Creative Co-Op",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Whitewash wood box is the specific form featured in centerpiece-wooden-box and wooden-centerpiece-boxes articles",
            "Side handles make it practical as a seasonal decoration — move it from table to sideboard without rearranging the contents",
        ],
        "default_cons": [
            "Whitewash shows water rings from condensation if used to hold a vase directly — use a liner",
        ],
        "notes_for_writers": NOTE,
    },

    "torre-tagus-pillar-ceramic-vase-white": {
        "name": "Torre & Tagus Pillar Ceramic Vase White",
        "brand": "Torre & Tagus",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Tall pillar form is the most versatile for table-centerpieces-for-home articles — works with tall branches or a single large stem",
            "Matte white ceramic coordinates with any table colour scheme",
        ],
        "default_cons": [
            "Tall form requires a table long enough not to obstruct sightlines across the dinner table",
        ],
        "notes_for_writers": NOTE,
    },

    "creative-co-op-mango-wood-bud-vase-set3": {
        "name": "Creative Co-Op Mango Wood Bud Vase Set of 3",
        "brand": "Creative Co-Op",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Mango wood grain is visible through the natural finish — the organic texture that wood-vases-for-centerpieces articles target",
            "Set of 3 in varying heights allows cluster arrangement without matching pieces exactly",
        ],
        "default_cons": [
            "Wood is not waterproof — requires a glass tube insert to hold water, which adds to the setup time",
        ],
        "notes_for_writers": NOTE,
    },

    "simon-pearce-woodstock-vase": {
        "name": "Simon Pearce Woodstock Vase",
        "brand": "Simon Pearce",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Mouth-blown in Vermont — the organic form and slight asymmetry that distinguishes it from machine-cast glass",
            "Heavy base makes it stable with large stem arrangements — not a tipping risk",
        ],
        "default_cons": [
            "Hand-blown glass requires hand-washing — a significant consideration for a vase cleaned regularly after flower use",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Decor: Candles ────────────────────────────────────────────────────────

    "root-candles-timberline-taper-set12": {
        "name": "Root Candles Timberline Collenette Taper Candles Set of 12",
        "brand": "Root Candles",
        "hub": "decor",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Timberline Collenette tapers are available in over 30 colours including blue, burgundy, gold, and white — the assortment that covers multiple colour-specific taper candle articles in one SKU",
            "Crafted in Ohio from pure beeswax blend — burns without the black soot of paraffin tapers",
        ],
        "default_cons": [
            "Beeswax blend is firmer than paraffin — may require brief warming in hand to fit a tight candle holder",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Serveware: Serving Platters ───────────────────────────────────────────

    "godinger-silver-round-serving-platter": {
        "name": "Godinger Silver Round Serving Platter 16-Inch",
        "brand": "Godinger",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "Silver-tone finish reads as antique silver at a fraction of the cost — covers silver-serving-platters-antique and metal-platters-serving articles",
            "16-inch diameter is the practical minimum for a full cheese board or cold appetiser spread",
        ],
        "default_cons": [
            "Silver-tone finish can scratch from metal utensils — use serving pieces with silicone-coated tips",
        ],
        "notes_for_writers": NOTE,
    },

    "certified-intl-talavera-serving-platter": {
        "name": "Certified International Talavera Ceramic Serving Platter 14-Inch",
        "brand": "Certified International",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Hand-painted Talavera motif in cobalt and terracotta is the reference aesthetic for mexican-serving-platters articles",
            "Ceramic construction is dishwasher safe despite the decorative surface",
        ],
        "default_cons": [
            "Decorative pattern limits it to Mexican and Southwestern table settings",
        ],
        "notes_for_writers": NOTE,
    },

    "juliska-berry-thread-ceramic-platter": {
        "name": "Juliska Berry & Thread Ceramic Serving Platter",
        "brand": "Juliska",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Hand-crafted whitewash stoneware with the berry-and-thread relief motif — the premium reference for colorful-serving-platters and handmade-ceramic-serving-platters articles",
            "Coordinates with the full Juliska dinnerware, linen, and entertaining collection",
        ],
        "default_cons": [
            "Hand-wash recommended to preserve the hand-applied relief detail",
        ],
        "notes_for_writers": NOTE,
    },

    "lenox-french-perle-blue-oval-platter": {
        "name": "Lenox French Perle Blue Oval Platter 16-Inch",
        "brand": "Lenox",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "French Perle Blue is the most-collected Lenox entertaining pattern — covers oval-serving-platters and large-ceramic-serving-platters articles",
            "Coordinates with the French Perle White Platter already in the catalog — allows buyers to mix colours in the same pattern",
        ],
        "default_cons": [
            "Sold as a single piece — an entertaining set requires collecting multiple items individually",
        ],
        "notes_for_writers": NOTE,
    },

    "michael-aram-olive-branch-serving-platter": {
        "name": "Michael Aram Olive Branch Serving Platter",
        "brand": "Michael Aram",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Hand-crafted oxidised nickel with cast olive branch relief — the decorative serving piece for antique-serving-platters and old-serving-platters articles",
            "Michael Aram's sculptural pieces have strong secondary market value — the brand that commands a premium for its narrative",
        ],
        "default_cons": [
            "Hand-wash only; the oxidised finish reacts to dishwasher detergent",
        ],
        "notes_for_writers": NOTE,
    },

    # ── Serveware: Place Cards ────────────────────────────────────────────────

    "mud-pie-porcelain-place-cards-set12": {
        "name": "Mud Pie White and Gold Porcelain Place Cards Set of 12",
        "brand": "Mud Pie",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "mid",
        "default_pros": [
            "Porcelain place cards are reusable and coordinate with fine china — the specific product form for porcelain-place-cards articles",
            "Gold-edge detail makes them formal enough for a seated dinner without being fussy",
        ],
        "default_cons": [
            "Writing surfaces require a fine-tip china marker — standard pens do not adhere to the glazed surface",
        ],
        "notes_for_writers": NOTE,
    },

    "kate-aspen-gold-foil-place-cards-set50": {
        "name": "Kate Aspen Gold Foil Foldable Place Cards Set of 50",
        "brand": "Kate Aspen",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "budget",
        "default_pros": [
            "50-pack at budget pricing covers a large event — the practical choice for foldable-place-cards and folded-place-cards articles",
            "Gold foil border makes disposable cards look intentional rather than improvised",
        ],
        "default_cons": [
            "Single-use disposable — not a reusable option for recurring dinner parties",
        ],
        "notes_for_writers": NOTE,
    },

    "juliska-country-estate-place-card-holders-set4": {
        "name": "Juliska Country Estate Place Card Holders Set of 4",
        "brand": "Juliska",
        "hub": "serveware",
        "amazon_asin": "VERIFY",
        "price_band": "premium",
        "default_pros": [
            "Country Estate ceramic holder coordinates with Juliska's dinnerware, linens, and serveware for a fully unified table",
            "Reusable — the investment case for premium place card holders over disposable paper cards",
        ],
        "default_cons": [
            "Premium price for a small accessory means they are a considered purchase rather than an impulse buy",
        ],
        "notes_for_writers": NOTE,
    },
}


def main():
    tmp_path = PRODUCTS_PATH + ".tmp"
    bak_path = PRODUCTS_PATH + ".bak"

    with open(PRODUCTS_PATH, "r") as f:
        existing = yaml.safe_load(f)
        f.seek(0)
        raw_header = ""
        for line in f:
            if line.startswith("#"):
                raw_header += line
            else:
                break

    conflicts = set(NEW_PRODUCTS.keys()) & set(existing.keys())
    if conflicts:
        print(f"ERROR: slug conflicts: {conflicts}")
        raise SystemExit(1)

    merged = {**existing, **NEW_PRODUCTS}

    # Re-read raw file to preserve header comments
    with open(PRODUCTS_PATH, "r") as f:
        original_raw = f.read()

    # Separate header (comment block at top)
    header_lines = []
    for line in original_raw.splitlines():
        if line.startswith("#") or line == "":
            header_lines.append(line)
        else:
            break
    header = "\n".join(header_lines) + "\n\n"

    # Dump only new products as YAML appendix
    new_yaml = yaml.dump(NEW_PRODUCTS, default_flow_style=False, allow_unicode=True, sort_keys=True, width=120)

    # Write to tmp: original + appended new entries
    with open(tmp_path, "w") as f:
        f.write(original_raw.rstrip("\n") + "\n\n")
        f.write("# ── Catalog Growth 2026-05-05 (" + str(len(NEW_PRODUCTS)) + " entries added) ─────────────────────────────────\n\n")
        f.write(new_yaml)

    # Validate parse
    with open(tmp_path) as f:
        check = yaml.safe_load(f)
    assert len(check) == len(existing) + len(NEW_PRODUCTS), f"Count mismatch: expected {len(existing)+len(NEW_PRODUCTS)}, got {len(check)}"

    # Atomic swap
    shutil.copy2(PRODUCTS_PATH, bak_path)
    shutil.move(tmp_path, PRODUCTS_PATH)

    print(f"Written: {PRODUCTS_PATH}")
    print(f"Backup:  {bak_path}")
    print(f"Before:  {len(existing)} products")
    print(f"Added:   {len(NEW_PRODUCTS)} products")
    print(f"After:   {len(check)} products")


if __name__ == "__main__":
    main()
