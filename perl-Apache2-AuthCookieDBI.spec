%define module Apache2-AuthCookieDBI

Name:		perl-%{module}
Version:	2.03
Release:    %mkrel 4
Summary:	An AuthCookie module backed by a DBI database
License:	LGPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/Apache2/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Apache::DBI) >= 0.91
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Apache2::AuthCookieDBI is a module that subclasses Apache2::AuthCookie and is
designed to be directly used for authentication in a mod_perl server.

It is a ticket-issuing system that looks up username/passwords in a DBI
database using generic SQL and issues MD5-checksummed tickets valid for
a configurable time period.  Incoming requests with tickets are
checksummed and expire-time checked.


%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README eg *.txt *.sql
%{perl_vendorlib}/Apache2
%{_mandir}/*/*
