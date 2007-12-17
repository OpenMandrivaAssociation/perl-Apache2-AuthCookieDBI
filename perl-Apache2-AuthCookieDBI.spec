%define real_name Apache2-AuthCookieDBI

Summary:	Apache2::AuthCookieDBI - An AuthCookie module backed by a DBI database
Name:		perl-%{real_name}
Version:	2.03
Release: %mkrel 2
License:	LGPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Apache::DBI) >= 0.91
BuildArch:	noarch

%description
Apache2::AuthCookieDBI is a module that subclasses Apache2::AuthCookie and is
designed to be directly used for authentication in a mod_perl server.

It is a ticket-issuing system that looks up username/passwords in a DBI
database using generic SQL and issues MD5-checksummed tickets valid for
a configurable time period.  Incoming requests with tickets are
checksummed and expire-time checked.


%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README eg *.txt *.sql
%{perl_vendorlib}/Apache2/AuthCookieDBI.pm
%{_mandir}/*/*



