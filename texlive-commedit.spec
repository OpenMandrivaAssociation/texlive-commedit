Name:		texlive-commedit
Version:	50116
Release:	2
Summary:	Commented editions with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/commedit
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commedit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commedit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commedit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is intended for commented editions. An example of
commented edition is a teacher's book based on a student's
textbook. Each page of a teacher's book is a page from the
textbook and comments for the teacher. This package was
commissioned by Instituto de Matematica Pura e Aplicada ( IMPA)

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/commedit
%{_texmfdistdir}/tex/latex/commedit
%doc %{_texmfdistdir}/doc/latex/commedit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
