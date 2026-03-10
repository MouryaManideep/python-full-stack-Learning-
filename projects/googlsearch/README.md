# Google Search URL Examples

This file shows how **Google search URLs work** and how **query parameters** are used in different types of searches.

---

## Search

```
https://www.google.com/search
?q=Harvard
&rlz=1C1CHBF_enIN1071IN1071
&oq=
&gs_lcrp=EgZjaHJvbWUqCQgBEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIRCAMQABgDGEIYjwEYtAIY6gIyEQgEEAAYAxhCGI8BGLQCGOoCMhEIBRAAGAMYQhiPARi0AhjqAjIPCAYQLhgDGI8BGLQCGOoCMhEIBxAAGAMYQhiPARi0AhjqAtIBCTI2NjRqMGoxNagCCLACAfEF4PebEqPTePQ
&sourceid=chrome
&ie=UTF-8
```

Key parameter:

- `q=Harvard` → search keyword

---

## Search Image

```
https://www.google.com/search
?sca_esv=a57f38d8b1aff971
&rlz=1C1CHBF_enIN1071IN1071
&sxsrf=ANbL-n4_4cUeRey73izi7KLtfdEoj5jDGg:1773114354252
&udm=2
&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3ppPEReeCOS7s1VbbZz2TLsjAI19UTbB8tUxW5GcTtCbPX8sLbJS_I_2-w19Qfjq3WeQbO6Iw1BR60TKMhWiCgM8xKT16qOTweeE-c2t5YhEwJl1cTu5BZTE-SpQwGRo7EXKXng5PDhm4ymO_Ya8YWLd_flnkuyKsCZwFLDpVC6r05RK4g
&q=harvard
&sa=X
&ved=2ahUKEwigxezZtZSTAxWtzzgGHfPDERYQtKgLegQIDhAB
&biw=1536
&bih=791
&dpr=1.25
```

Key parameter:

- `q=harvard` → search query
- `udm=2` → image search mode

---

## Advanced Search

```
https://www.google.com/search
?as_q=digital+marketing+strategies
&as_epq=%22social+media+marketing%22
&as_oq=guide+tutorial
&as_eq=beginner
&as_nlo=
&as_nhi=
&lr=
&cr=
&as_qdr=all
&as_sitesearch=
&as_occt=any
&as_filetype=
&tbs=
```

Key parameters:

- `as_q` → all these words
- `as_epq` → exact phrase
- `as_oq` → any of these words
- `as_eq` → exclude words

---

## Notes

- `?` starts the query parameters
- `&` separates parameters
- `parameter=value` defines search behavior
