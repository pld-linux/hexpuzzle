Summary:	Hex Puzzle 22
Summary(pl):	�amig��wka Hex Puzzle 22
Name:		hexpuzzle
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ibiblio.org/pub/Linux/games/%{name}-%{version}.tgz
# Source0-md5:	b807ab119697b295dd7e2a856522730d
Patch0:		%{name}-datadir.patch
URL:		ftp://ibiblio.org/pub/Linux/games/
Requires:	tk >= 8.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hex Puzzle 22 is a tessellation puzzle based on Beat The Computer #22.
Players must fit all of the multi-hexagon pieces into one of three
different trays.

%description -l pl
Hex Puzzle 22 to uk�adanka oparta na Beat The Computer #22. Gracze
musz� dopasowa� wszystkie kawa�ki sk�adaj�ce si� z sze�ciok�t�w do
jednej z trzech r�nych tac.

%prep
%setup -q -n %{name}
%patch -p1

%clean
rm -rf $RPM_BUILD_ROOT

%build
mv -f hexpuzzle{,~}
sed 's#@@DATADIR@@#%{_datadir}/%{name}#g' <hexpuzzle~ >hexpuzzle

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install hexpuzzle $RPM_BUILD_ROOT%{_bindir}
install pieces.* $RPM_BUILD_ROOT%{_datadir}/%{name}
install menus $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%defattr(644,root,root,755)
%doc About Bugs Changelog Instructions Readme Thanks Todo
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
