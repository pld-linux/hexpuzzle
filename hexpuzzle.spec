Summary:	Hex Puzzle 22
Summary(pl):	--
Name:		hexpuzzle
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ibiblio.org/pub/Linux/games/%{name}-%{version}.tgz
# Source0-md5:	b807ab119697b295dd7e2a856522730d
Patch0:		%{name}-datadir.patch
URL:		ftp://ibiblio.org/pub/Linux/games
Requires:	tk
BuildRequires:	sed
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hex Puzzle 22 is a tessellation puzzle based on Beat The Computer #22.
Players must fit all of the multi-hexagon pieces into one of three
different trays.

%description -l pl
-

%prep
%setup -q -n %{name}
%patch -p1

%clean
rm -rf $RPM_BUILD_ROOT

%build
mv hexpuzzle{,~}
sed 's#@@DATADIR@@#%{_datadir}/%{name}#g' <hexpuzzle~ >hexpuzzle

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_docdir}}
install hexpuzzle $RPM_BUILD_ROOT%{_bindir}
install pieces.* $RPM_BUILD_ROOT%{_datadir}/%{name}
install menus $RPM_BUILD_ROOT%{_datadir}/%{name}
install [A-Z]* $RPM_BUILD_ROOT%{_docdir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*
%doc %{_docdir}
