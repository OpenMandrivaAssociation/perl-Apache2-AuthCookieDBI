%define upstream_name    Apache2-AuthCookieDBI
%define upstream_version 2.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	An AuthCookie module backed by a DBI database
License:	LGPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache2/Apache2-AuthCookieDBI-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Apache::DBI) >= 0.91
BuildRequires:	perl(Date::Calc)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	apache-mod_perl
BuildArch:	noarch

%description
Apache2::AuthCookieDBI is a module that subclasses Apache2::AuthCookie and is
designed to be directly used for authentication in a mod_perl server.

It is a ticket-issuing system that looks up username/passwords in a DBI
database using generic SQL and issues MD5-checksummed tickets valid for
a configurable time period.  Incoming requests with tickets are
checksummed and expire-time checked.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README eg *.txt *.sql
%{perl_vendorlib}/Apache2
%{_mandir}/*/*


%changelog
* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.140.0-1mdv2011.0
+ Revision: 649132
- update to new version 2.14

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.130.0-1mdv2011.0
+ Revision: 622947
- update to new version 2.13

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.50.0-1mdv2011.0
+ Revision: 402969
- rebuild using %%perl_convert_version

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdv2010.0
+ Revision: 377832
- update to new version 2.05

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-1mdv2009.1
+ Revision: 309442
- update to new version 2.04

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.03-6mdv2009.0
+ Revision: 255267
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-4mdv2008.1
+ Revision: 136945
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-3mdv2008.1
+ Revision: 136883
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.03-2mdv2007.0
+ Revision: 73243
- import perl-Apache2-AuthCookieDBI-2.03-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.03-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 2.03-1mdk
- initial Mandriva package


