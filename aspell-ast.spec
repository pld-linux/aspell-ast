Summary:	Asturian dictionary for aspell
Summary(pl.UTF-8):	Słownik asturski dla aspella
Name:		aspell-ast
Version:	0.01
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ast/aspell6-ast-%{version}.tar.bz2
# Source0-md5:	28955414fef2bc3e5395d45e051bdcd9
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asturian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik asturski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-ast-%{version}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/aspell/ast.*
%{_libdir}/aspell/asturianu.alias
%{_datadir}/aspell/ast.dat
%{_datadir}/aspell/ast_affix.dat
%{_datadir}/aspell/l-ast.*
