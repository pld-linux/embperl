%include	/usr/lib/rpm/macros.perl
Summary:	Embedded perl - building dynamic Websites with Perl
Summary(pl):	Osadzony perl - budowanie dynamicznych stron przy u�yciu Perla
Name:		embperl
Version:	1.3.6
Release:	3
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.dev.ecos.de/pub/perl/embperl/HTML-Embperl-%{version}.tar.gz
# Source0-md5:	b360a0f9ba5d5e35f6426c81dd91933d
Patch0:		%{name}-makefile.patch
BuildRequires:	apache-devel >= 2.0
BuildRequires:	apache-mod_perl >= 2.0
BuildRequires:	perl-devel
BuildRequires:	perl-Apache-Session
BuildRequires:	perl(CGI)
BuildRequires:	perl-HTML-HeadParser
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(CGI)'

%description
Embperl gives you the power to embed Perl code in your HTML documents
and the ability to build your Web site out of small reusable objects
in a OO-style. You can also take advantage all available Perl modules,
(including DBI for database access) use their functionality and easily
include their output into your web pages.

%description -l pl
Embperl daje moc zagnie�d�ania kodu Perla w dokumentach HTML i
mo�liwo�� budowania stron WWW z ma�ych obiekt�w. Mo�na wykorzysta�
wszystkie dost�pne modu�y Perla (w tym DBI do dost�pu do baz danych).

%prep
%setup -q -n HTML-Embperl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} CFLAGS="%{rpmcflags}"
cp eg/README README.examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir},%{_docdir}/eg}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO README.examples
%attr(755,root,root) %{_bindir}/*.pl
%{perl_vendorarch}/HTML/Embperl*
%dir %{perl_vendorarch}/auto/HTML/Embperl
%{perl_vendorarch}/auto/HTML/Embperl/Embperl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Embperl/Embperl.so
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
