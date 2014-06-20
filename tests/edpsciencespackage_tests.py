# -*- coding: utf-8 -*-
##
## This file is part of Harvesting Kit.
## Copyright (C) 2014 CERN.
##
## Harvesting Kit is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Harvesting Kit is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Harvesting Kit; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
import unittest
from harvestingkit.edpsciences_package import EDPSciencesPackage
from xml.dom.minidom import parse


sample_record = "sample_edpsciences_record.xml"


class EDPSciencesPackageTests(unittest.TestCase):
    def setUp(self):
        self.edp = EDPSciencesPackage()
        self.edp.document = parse(sample_record)

    def test_abstract(self):
        abstract = 'Context. The depletion of iron and sulphur into dust in '\
                   'the interstellar medium and the exact nature of interstellar '\
                   'amorphous silicate grains is still an open question. Aims. We '\
                   'study the incorporation of iron and sulphur into amorphous '\
                   'silicates of olivine- and pyroxene-types and their effects on '\
                   'the dust spectroscopy and thermal emission. Methods. We used '\
                   'the Maxwell-Garnett effective-medium theory to construct the '\
                   'optical constants for a mixture of silicates, metallic iron, '\
                   'and iron sulphide. We also studied the effects of iron and '\
                   'iron sulphide in aggregate grains. Results. Iron sulphide '\
                   'inclusions within amorphous silicates that contain iron metal '\
                   'inclusions show no strong differences in the optical properties '\
                   'of the grains. A mix of amorphous olivine- and pyroxene-type '\
                   'silicate broadens the silicate features. An amorphous carbon mantle '\
                   'with a thickness of 10 nm on the silicate grains leads to an increase '\
                   'in absorption on the short-wavelength side of the 10 μ m silicate band. '\
                   'Conclusions. The assumption of amorphous olivine-type and pyroxene-type '\
                   'silicates and a 10 nm thick amorphous carbon mantle better matches the '\
                   'interstellar silicate band profiles. Including iron nano-particles leads '\
                   'to an increase in the mid-IR extinction, while up to 5 ppm of sulphur can '\
                   'be incorporated as Fe/FeS nano inclusions into silicate grains without leaving '\
                   'a significant trace of its presence.'
        self.assertEqual(self.edp._get_abstract(), abstract)

    def test_journal(self):
        self.assertEqual(self.edp._get_journal(), 'Astron.Astrophys.')

    def test_publisher(self):
        self.assertEqual(self.edp._get_publisher(), 'EDP Sciences')

    def test_date(self):
        self.assertEqual(self.edp._get_date(), '2014-05-23')

    def test_title(self):
        title = 'A hidden reservoir of Fe/FeS in interstellar silicates?'
        self.assertEqual(self.edp._get_title(), title)

    def test_doi(self):
        self.assertEqual(self.edp._get_doi(), u'10.1051/0004-6361/201423985')

    def test_page_count(self):
        self.assertEqual(self.edp._get_page_count(), u'4')

    def test_authors(self):
        authors = [('Krause, Martin', [u'AFF1', u'AFF2'], ''),
                   ('K\xc3\xb6hler, M.', [], ''),
                   ('Jones, A.', [], ''),
                   ('Ysard, N.', [], '')]
        self.assertEqual(self.edp._get_authors(), authors)

    def test_pacscodes(self):
        self.assertEqual(self.edp._get_pacscodes(), [])

    def test_copyright(self):
        self.assertEqual(self.edp._get_copyright(), ('ESO', '2014', '\xc2\xa9 ESO, 2014'))

    def test_publication_information(self):
        publication_information = ('Astron.Astrophys.',
                                   '565',
                                   '',
                                   u'2014',
                                   '2014-05-23',
                                   u'10.1051/0004-6361/201423985',
                                   'L9',
                                   '925',
                                   '')
        self.assertEqual(self.edp._get_publication_information(), publication_information)

    def test_affiliations(self):
        affiliations = {u'AFF1': 'Institut d\xe2\x80\x99Astrophysique Spatiale (IAS), Universit\xc3\xa9 Paris-Sud & CNRS , B\xc3\xa2t. 121 , 91405 Orsay , France',
                        u'AFF2': 'Excellence Cluster Universe, Technische Universit\xc3\xa4t M\xc3\xbcnchen , Boltzmannstrasse 2 , 85748 Garching , Germany'}
        self.assertEqual(self.edp._get_affiliations(), affiliations)

    def test_author_emails(self):
        author_emails = {u'FN1': ['mkoehler@ias.u-psud.fr']}
        self.assertEqual(self.edp._get_author_emails(), author_emails)

    def test_subject(self):
        self.assertEqual(self.edp._get_subject(), '')

    def test_license(self):
        self.assertEqual(self.edp._get_license(), ('Creative Commons Attribution License 2.0', 'open-access'))

    def test_references(self):
        references = [(u'other', 'Bohren, C., & Huffman, D. 1983, Absorption and Scattering of Light by Small Particles (New York: Wiley and Sons)', '', [], '', '', '', ''),
                      (u'journal', '', '', ['Bradley, J.P.'], '1994', 'Science', '265', '925'),
                      (u'journal', '', '', ['Caselli, P.', 'Hasegawa, T.I.', 'Herbst, E.'], '1994', 'Astrophys.J.', '421', '206'),
                      (u'journal', '', '', ['Chiar, J.E.', 'Tielens, A.G.G.M.'], '2006', 'Astrophys.J.', '637', '774'),
                      (u'journal', '', '', ['Compi\xc3\xa8gne, M.', 'Verstraete, L.', 'Jones, A.'], '2011', 'Astron.Astrophys.', '525', 'A103'),
                      (u'journal', '', '', ['Costantini, E.', 'Freyberg, M.J.', 'Predehl, P.'], '2005', 'Astron.Astrophys.', '444', '187'),
                      (u'journal', '', '', ['Davoisne, C.', 'Djouadi, Z.', 'Leroux, H.'], '2006', 'Astron.Astrophys.', '448', 'L1'),
                      (u'journal', '', '', ['Demyk, K.', 'Carrez, P.', 'Leroux, H.'], '2001', 'Astron.Astrophys.', '368', 'L38'),
                      (u'journal', '', '', ['Djouadi, Z.', 'Gattacceca, J.', 'D\xe2\x80\x99Hendecourt, L.'], '2007', 'Astron.Astrophys.', '468', 'L9'),
                      (u'journal', '', '', ['Draine, B.'], '1988', 'Astrophys.J.', '333', '848'),
                      (u'other', 'Draine, B. T., & Flatau, P. J. 2010, unpublished [ arXiv:1002.1505 ]', 'arXiv:1002.1505', [], '', '', '', ''),
                      (u'journal', '', '', ['Jenkins, E.B.'], '2009', 'Astrophys.J.', '700', '1299'),
                      (u'journal', '', '', ['Jones, A.P.'], '2000', 'J.Geophys.Res.', '105', '10257'),
                      (u'journal', '', '', ['Jones, A.P.'], '2011', 'Astron.Astrophys.', '528', 'A98'),
                      (u'journal', '', '', ['Jones, R.V.', 'Spitzer, L.'], '1967', 'Astrophys.J.', '147', '943'),
                      (u'journal', '', '', ['Jones, A.P.', 'Fanciullo, L.', 'K\xc3\xb6hler, M.'], '2013', 'Astron.Astrophys.', '558', 'A62'),
                      (u'journal', '', '', ['Joseph, C.L.', 'Snow, T.P.', 'Seab, C.G.', 'Crutcher, R.M.'], '1986', 'Astrophys.J.', '309', '771'),
                      (u'journal', '', '', ['Keller, L.P.', 'Hony, S.', 'Bradley, J.P.'], '2002', 'Nature', '417', '148'),
                      (u'journal', '', '', ['Leroux, H.', 'Roskosz, M.', 'Jacob, D.'], '2009', 'Geochim.Cosmochim.Acta', '73', '767'),
                      (u'journal', '', '', ['Mathis, J.S.'], '1990', 'Ann.Rev.Astron.Astrophys.', '28', '37'),
                      (u'journal', '', '', ['McClure, M.'], '2009', 'Astrophys.J.', '693', 'L81'),
                      (u'journal', '', '', ['Millar, T.J.', 'Herbst, E.'], '1990', 'Astron.Astrophys.', '231', '466'),
                      (u'journal', '', '', ['Min, M.', 'Waters, L.B.F.M.', 'de Koter, A.'], '2007', 'Astron.Astrophys.', '462', '667'),
                      (u'journal', '', '', ['Nguyen, A.N.', 'Stadermann, F.J.', 'Zinner, E.'], '2007', 'Astrophys.J.', '656', '1223'),
                      (u'journal', '', '', ['Ordal, M.A.', 'Bell, R.J.', 'Alexander, R.W.', 'Long, L.L.', 'Querry, M.R.'], '1985', 'Appl.Opt.', '24', '4493'),
                      (u'journal', '', '', ['Ordal, M.A.', 'Bell, R.J.', 'Alexander, R.W.', 'Newquist, L.A.', 'Querry, M.R.'], '1988', 'Appl.Opt.', '27', '1203'),
                      (u'other', 'Planck Collaboration XI 2014, A&A, in press [ arXiv:1312.1300 ]', 'arXiv:1312.1300', [], '', '', '', ''),
                      (u'journal', '', '', ['Pollack, J.B.', 'Hollenbach, D.', 'Beckwith, S.'], '1994', 'Astrophys.J.', '421', '615'),
                      (u'journal', '', '', ['Purcell, E.M.', 'Pennypacker, C.R.'], '1973', 'Astrophys.J.', '186', '705'),
                      (u'journal', '', '', ['Rieke, G.H.', 'Lebofsky, M.J.'], '1985', 'Astrophys.J.', '288', '618'),
                      (u'journal', '', '', ['Roskosz, M.', 'Gillot, J.', 'Capet, F.', 'Roussel, P.', 'Leroux, H.'], '2011', 'Astron.Astrophys.', '529', 'A111'),
                      (u'journal', '', '', ['Savage, B.D.', 'Bohlin, R.C.'], '1979', 'Astrophys.J.', '229', '136'),
                      (u'journal', '', '', ['Savage, B.D.', 'Mathis, J.S.'], '1979', 'Ann.Rev.Astron.Astrophys.', '17', '73'),
                      (u'journal', '', '', ['Scott, A.', 'Duley, W.W.'], '1996', 'Astrophys.J.Suppl.', '105', '401'),
                      (u'journal', '', '', ['Sofia, U.J.', 'Joseph, C.L.'], '1995', 'Bull.Am.Astron.Soc.', '27', '860'),
                      (u'journal', '', '', ['Ueda, Y.', 'Mitsuda, K.', 'Murakami, H.', 'Matsushita, K.'], '2005', 'Astrophys.J.', '620', '274'),
                      (u'journal', '', '', ['Xiang, J.', 'Lee, J.C.', 'Nowak, M.A.', 'Wilms, J.'], '2011', 'Astrophys.J.', '738', '78')]
        for ref in self.edp._get_references():
            self.assertTrue(ref in references)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EDPSciencesPackageTests)
    unittest.TextTestRunner(verbosity=2).run(suite)