%global tl_name altfont
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Alternative font handling in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/altfont
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a replacement for that part of psnfss and mfnfss
that changes the default font. The package is distributed together with
the psfont package, by the same author.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/altfont
%dir %{_datadir}/texmf-dist/source/latex/altfont
%dir %{_datadir}/texmf-dist/tex/latex/altfont
%doc %{_datadir}/texmf-dist/doc/latex/altfont/README
%doc %{_datadir}/texmf-dist/doc/latex/altfont/altfont.pdf
%doc %{_datadir}/texmf-dist/doc/latex/altfont/psfont.pdf
%doc %{_datadir}/texmf-dist/source/latex/altfont/altfont.dtx
%doc %{_datadir}/texmf-dist/source/latex/altfont/altfont.ins
%doc %{_datadir}/texmf-dist/source/latex/altfont/psfont.dtx
%doc %{_datadir}/texmf-dist/source/latex/altfont/psfont.ins
%{_datadir}/texmf-dist/tex/latex/altfont/altfont.cfg
%{_datadir}/texmf-dist/tex/latex/altfont/altfont.sty
%{_datadir}/texmf-dist/tex/latex/altfont/psfont.cfg
%{_datadir}/texmf-dist/tex/latex/altfont/psfont.sty
