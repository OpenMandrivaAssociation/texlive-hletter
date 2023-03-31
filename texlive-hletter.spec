Name:		texlive-hletter
Version:	30002
Release:	2
Summary:	Flexible letter typesetting with flexible page headings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hletter
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hletter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hletter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package permits the user to specify easily, with the aid of
self defined key-words, letters (with a logo and private) and
headings. The heading may include a footer and the letter
provides commands to include a scanned signature and two
signees. The package works with the merge package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hletter/hdefine.clo
%{_texmfdistdir}/tex/latex/hletter/hhead.sty
%{_texmfdistdir}/tex/latex/hletter/hlete.clo
%{_texmfdistdir}/tex/latex/hletter/hletf.clo
%{_texmfdistdir}/tex/latex/hletter/hletg.clo
%{_texmfdistdir}/tex/latex/hletter/hletter.cls
%{_texmfdistdir}/tex/latex/hletter/hsetup.sty
%{_texmfdistdir}/tex/latex/hletter/mergeh.sty
%doc %{_texmfdistdir}/doc/latex/hletter/Bruennhilde.eps
%doc %{_texmfdistdir}/doc/latex/hletter/Bruennhilde.jpg
%doc %{_texmfdistdir}/doc/latex/hletter/Gccs.eps
%doc %{_texmfdistdir}/doc/latex/hletter/Gccs.jpg
%doc %{_texmfdistdir}/doc/latex/hletter/Hletter.pdf
%doc %{_texmfdistdir}/doc/latex/hletter/README
%doc %{_texmfdistdir}/doc/latex/hletter/Testheader.tex
%doc %{_texmfdistdir}/doc/latex/hletter/Testletter1.tex
%doc %{_texmfdistdir}/doc/latex/hletter/Testletter2.tex
%doc %{_texmfdistdir}/doc/latex/hletter/Testletter3.tex
%doc %{_texmfdistdir}/doc/latex/hletter/Testmerge.dat
%doc %{_texmfdistdir}/doc/latex/hletter/Testmerge.tex
%doc %{_texmfdistdir}/doc/latex/hletter/signat.eps
%doc %{_texmfdistdir}/doc/latex/hletter/signat.jpg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
