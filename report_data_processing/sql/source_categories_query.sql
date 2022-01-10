SELECT
    published_year,
    type,
    field,
    COUNT(DISTINCT doi) as num_dois,

    {% for item in data_items -%}
    , COUNT(DISTINCT IF(has_{{ item }}, doi, null)) as dois_with_{{ item }}
    {% endfor -%}
    , COUNT(DISTINCT IF(doi_not_canonical_family, doi, null)) as doi_not_canonical_family

    {% for item in data_items -%}
    , COUNT(DISTINCT IF(has_{{ item }}, source_id, null)) as objects_with_{{ item }}
    {% endfor %}

FROM {{table}}
GROUP BY published_year, type, field
ORDER BY published_year DESC, type ASC, field ASC
