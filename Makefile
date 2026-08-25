main.pdf: main.tex
	latexmk -pdflua -silent $<
