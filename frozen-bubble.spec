%include	/usr/lib/rpm/macros.perl
Summary:	Frozen Bubble arcade game
Summary(pl):	Gra zrêczno¶ciowa Frozen Bubble
Name:		frozen-bubble
Version:	2.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.frozen-bubble.org/data/%{name}-%{version}.tar.bz2
# Source0-md5:	9fdd84f56e5221e6c58c12eab72459d9
Source1:	%{name}.desktop
Patch0:		%{name}-make.patch
URL:		http://www.frozen-bubble.org/
BuildRequires:	SDL_Pango-devel
BuildRequires:	SDL_mixer-devel >= 1.2.2
BuildRequires:	perl-SDL >= 2.1.0
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	smpeg-devel
Requires:	perl(Locale::gettext) >= 1.04
Requires:	perl-SDL >= 2.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(fbmdkcommon)' 'perl(Gimp)'

%description
Full-featured, colorful animated penguin eyecandy, 50 levels of 1p
game, hours and hours of 2p game, 3 professional quality 20-channels
musics, 15 stereo sound effects, 7 unique graphical transition
effects.

%description -l pl
Gra o wielu mo¿liwo¶ciach, z kolorowymi animacjami, 50-ma poziomami
dla jednego gracza, wieloma godzinami zabawy dla dwóch graczy, 3-ma
profesjonalnej jako¶ci 20-kana³owymi muzyczkami, 15-ma
stereofonicznymi efektami d¼wiêkowymi, 7-ma unikalnymi graficznymi
efektami przej¶æ.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	OPTIMIZE="%{rpmcflags} -Wall" \
	OTHERLDFLAGS="%{rpmldflags}" \
	CC="%{__cc}" \
	PREFIX="%{_prefix}" \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	PREFIX="%{_prefix}" \
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
%{perl_vendorarch}/auto/fb_c_stuff/fb_c_stuff.bs
%attr(755,root,root) %{perl_vendorarch}/auto/fb_c_stuff/fb_c_stuff.so
%{perl_vendorarch}/*.pm
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man6/*
