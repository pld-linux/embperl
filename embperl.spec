%include	/usr/lib/rpm/macros.perl
Summary:	Embedded perl - building dynamic Websites with Perl
Summary(pl):	Osadzony perl - budowanie dynamicznych stron przy u¿yciu Perla
Name:		embperl
Version:	1.3.3
Release:	3
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.dev.ecos.de/pub/perl/embperl/HTML-Embperl-%{version}.tar.gz
# Source0-md5:	f2a4579210f7797e1ff4d756f3b7e037
Patch0:		%{name}-makefile.patch
BuildRequires:	apache-devel
BuildRequires:	apache-mod_perl
BuildRequires:	apache-mod_actions
BuildRequires:	perl-devel
BuildRequires:	perl(Apache::Session)
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::HeadParser)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(File::Spec)
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embperl gives you the power to embed Perl code in your HTML documents
and the ability to build your Web site out of small reusable objects
in a OO-style. You can also take advantage all available Perl modules,
(including DBI for database access) use their functionality and easily
include their output into your web pages.

%description -l pl
Embperl daje moc zagnie¿d¿ania kodu Perla w dokumentach HTML i
mo¿liwo¶æ budowania stron WWW z ma³ych obiektów. Mo¿na wykorzystaæ
wszystkie dostêpne modu³y Perla (w tym DBI do dostêpu do baz danych).

%prep
%setup -q -n HTML-Embperl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO eg/README
%attr(755,root,root) %{_bindir}/*.pl
%{perl_vendorarch}/HTML/Embperl*
%dir %{perl_vendorarch}/auto/HTML/Embperl
%{perl_vendorarch}/auto/HTML/Embperl/Embperl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Embperl/Embperl.so
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
