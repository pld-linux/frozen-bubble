%include	/usr/lib/rpm/macros.perl
Summary:	Frozen Bubble arcade game
Summary(pl.UTF-8):	Gra zręcznościowa Frozen Bubble
Name:		frozen-bubble
Version:	2.2.0
Release:	8
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.frozen-bubble.org/data/%{name}-%{version}.tar.bz2
# Source0-md5:	f7987201470d6755ed309762d348e0dd
Source1:	%{name}.desktop
Patch0:		%{name}-make.patch
Patch1:		%{name}-kill-warning.patch
URL:		http://www.frozen-bubble.org/
BuildRequires:	SDL_Pango-devel
BuildRequires:	SDL_mixer-devel >= 1.2.2
BuildRequires:	gettext-tools
BuildRequires:	perl-SDL >= 2.1.0
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	smpeg-devel
Requires:	perl-Locale-gettext >= 1.04
Requires:	perl-SDL >= 2.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(fbmdkcommon)' 'perl(Gimp)'

%description
Full-featured, colorful animated penguin eyecandy, 50 levels of 1p
game, hours and hours of 2p game, 3 professional quality 20-channels
musics, 15 stereo sound effects, 7 unique graphical transition
effects.

%description -l pl.UTF-8
Gra o wielu możliwościach, z kolorowymi animacjami, 50-ma poziomami
dla jednego gracza, wieloma godzinami zabawy dla dwóch graczy, 3-ma
profesjonalnej jakości 20-kanałowymi muzyczkami, 15-ma
stereofonicznymi efektami dźwiękowymi, 7-ma unikalnymi graficznymi
efektami przejść.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's/-Werror//' server/Makefile

%build
%{__make} \
	OPTIMIZE="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}" \
	CC="%{__cc}" \
	CPP="%{__cc} -E" \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

install icons/%{name}-icon-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx/.xvpics

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/frozen-bubble
%attr(755,root,root) %{_libdir}/frozen-bubble/fb-server
%{_datadir}/%{name}
%dir %{perl_vendorarch}/auto/fb_c_stuff
%attr(755,root,root) %{perl_vendorarch}/auto/fb_c_stuff/fb_c_stuff.so
%{perl_vendorarch}/*.pm
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man6/*
