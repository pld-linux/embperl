%include	/usr/lib/rpm/macros.perl
Summary:	Embedded perl - building dynamic Websites with Perl
Summary(pl):	Osadzony perl - budowanie dynamicznych stron przy u¿yciu Perla
Name:		embperl
Version:	1.3.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.dev.ecos.de/pub/perl/embperl/HTML-Embperl-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	apache-devel
BuildRequires:	perl-devel
BuildRequires:	perl(Apache::Session)
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::HeadParser)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(File::Spec)
Requires:	apache
Requires:	apache-mod_perl
Requires:	apache-mod_actions
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embperl gives you the power to embed Perl code in your HTML documents and
the ability to build your Web site out of small reusable objects in a
OO-style. You can also take advantage all available Perl modules, (including
DBI for database access) use their functionality and easily include their
output into your web pages.

%description -l pl

%prep
%setup -q -n HTML-Embperl-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO eg/README

cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*.pl
%{perl_sitearch}/HTML/Embperl*
%dir %{perl_sitearch}/auto/HTML/Embperl
%{perl_sitearch}/auto/HTML/Embperl/Embperl.bs
%attr(755,root,root) %{perl_sitearch}/auto/HTML/Embperl/Embperl.so
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}
