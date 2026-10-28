# Prompt Library

**Shared factual guardrail:** EcoSip Smart Bottle is a fictional reusable water bottle for everyday use, suitable for students and office workers, with water-level markings. Do not invent features, claims, certifications, statistics, testimonials, or environmental impact.

## Basic prompt — purpose: baseline output
Write one concise social media advertisement for the fictional EcoSip Smart Bottle. Product facts: reusable water bottle for everyday use, suitable for students and office workers, with water-level markings. Include a headline, short body, and call to action. Do not add other product claims.

## Role-based prompt — purpose: constrained audience/tone control
Act as an experienced advertising copywriter. Write one concise social-media ad for the fictional EcoSip Smart Bottle for college students and young professionals aged 18–30. Use a friendly, modern, practical, trustworthy tone. Use only these facts: reusable bottle; everyday use; suitable for students and office workers; water-level markings. Include headline, body (25–45 words), and clear call to action. Avoid unsupported claims and testimonials.

## Few-shot prompt — purpose: demonstrate tone and format
Write a new ad for the fictional EcoSip Smart Bottle, following the concise, friendly format of these examples without copying their wording: (1) “Pack your day, keep it simple. A small daily essential for the moments between class and home. Take a look.” (2) “Desk time, meet water time. A practical everyday companion for your workday. See what’s new.” Use only the verified project facts: reusable water bottle, everyday use, for students and office workers, water-level markings. Return headline, body, CTA. Avoid added claims.

## Responsible-AI verification prompt
Audit each ad against these facts only: fictional reusable bottle, everyday use, suitable for students and office workers, water-level markings. Flag unsupported features/claims, misleading language, testimonials, exaggerated promises, unclear CTA, confusing phrasing, similarity, and responsible advertising issues. Return original wording, issue, proposed correction, reason. Do not claim external verification.

## Ad-image generation prompt
Create a square social media advertisement for fictional EcoSip Smart Bottle: modern reusable bottle with visible water-level scale, clean student-friendly desk setting, sage and cream palette, readable headline “Make Every Sip Count.” and CTA “Meet Your Everyday Bottle.” Do not add unsupported claims or stats.

## Survey analysis prompt
Analyze only rows marked genuine/valid in the provided response data. Report valid n, votes by ad and prompt style, preference percentages, mean ratings and themes in open comments. Keep synthetic test rows excluded. If fewer than 20 valid genuine responses, state shortfall. If no real responses, say findings pending and declare no winner. Do not claim significance without suitable tests.

## Final report prompt
Write a capstone report using only supplied verified product facts and collected genuine survey data. Distinguish observations from inference, disclose sample size, missingness, limitations, and whether data is synthetic or real. When real data is absent, keep winner and findings pending.
