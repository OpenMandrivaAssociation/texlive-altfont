# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/altfont
# catalog-date 2007-09-25 20:36:22 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-altfont
Version:	1.1
Release:	1
Summary:	Alternative font handling in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/altfont
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altfont.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a replacement for that part of psnfss and
mfnfss that changes the default font. The package is
distributed together with the psfont package, by the same
author.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
