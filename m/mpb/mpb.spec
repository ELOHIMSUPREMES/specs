Name: mpb
Version: 1.4.2
Release: alt4
Summary: MIT Photonic Bands
License: GPLv2+
Group: Sciences/Physics
Url: http://ab-initio.mit.edu/wiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libctl-devel liblapack-devel zlib-devel
BuildPreReq: libreadline-devel libfftw-devel guile18 guile18-devel
BuildPreReq: gcc-fortran gcc-c++ /proc libhdf5-devel

%description
The MIT Photonic-Bands (MPB) package is a free program for computing the
band structures (dispersion relations) and electromagnetic modes of
periodic dielectric structures, on both serial and parallel computers.
It was developed by Steven G. Johnson at MIT along with the Joannopoulos
Ab Initio Physics group.

This program computes definite-frequency eigenstates (harmonic modes) of
Maxwell's equations in periodic dielectric structures for arbitrary
wavevectors, using fully-vectorial and three-dimensional methods. It is
especially designed for the study of photonic crystals (a.k.a. photonic
band-gap materials), but is also applicable to many other problems in
optics, such as waveguides and resonator systems. (For example, it can
solve for the modes of waveguides with arbitrary cross-sections.)

%package doc
Summary: Documentation for MIT Photonic Bands (MPB)
Group: Documentation
BuildArch: noarch

%description doc
The MIT Photonic-Bands (MPB) package is a free program for computing the
band structures (dispersion relations) and electromagnetic modes of
periodic dielectric structures, on both serial and parallel computers.
It was developed by Steven G. Johnson at MIT along with the Joannopoulos
Ab Initio Physics group.

This package contains documentation for MIT Photonic Bands (MPB).

%prep
%setup

rm -fR autom4te.cache

%build
%add_optflags -I%_includedir/ctl -I%_libdir/hdf5-seq/include
export CPPFLAGS="%optflags"

%autoreconf

%configure \
	--with-blas=-lopenblas \
	--with-lapack=-llapack \
	--with-inv-symmetry \
	--with-hermitian-eps \
	--with-libctl
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING COPYRIGHT NEWS README TODO
%_bindir/*
%_man1dir/*
%_datadir/libctl

%files doc
%doc doc/*

%changelog
* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4
- Rebuilt with new libhdf5

* Tue Oct 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt3
- Rebuilt with libctl 3.2.1
- Built with support of HDF5

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Thu Mar 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

