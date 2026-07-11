%global tl_name hletter
%global tl_revision 30002

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2
Release:	%{tl_revision}.1
Summary:	Flexible letter typesetting with flexible page headings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hletter
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hletter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hletter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package permits the user to specify easily, with the aid of self
defined key-words, letters (with a logo and private) and headings. The
heading may include a footer and the letter provides commands to include
a scanned signature and two signees. The package works with the merge
package.

