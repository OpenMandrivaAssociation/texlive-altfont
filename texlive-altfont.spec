Name:		texlive-altfont
Version:	15878
Release:	1
Summary:	Alternative font handling in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/altfont
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a replacement for that part of psnfss and
mfnfss that changes the default font. The package is
distributed together with the psfont package, by the same
author.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/altfont/altfont.cfg
%{_texmfdistdir}/tex/latex/altfont/altfont.sty
%{_texmfdistdir}/tex/latex/altfont/psfont.cfg
%{_texmfdistdir}/tex/latex/altfont/psfont.sty
%doc %{_texmfdistdir}/doc/latex/altfont/README
%doc %{_texmfdistdir}/doc/latex/altfont/altfont.pdf
%doc %{_texmfdistdir}/doc/latex/altfont/psfont.pdf
#- source
%doc %{_texmfdistdir}/source/latex/altfont/altfont.dtx
%doc %{_texmfdistdir}/source/latex/altfont/altfont.ins
%doc %{_texmfdistdir}/source/latex/altfont/psfont.dtx
%doc %{_texmfdistdir}/source/latex/altfont/psfont.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
