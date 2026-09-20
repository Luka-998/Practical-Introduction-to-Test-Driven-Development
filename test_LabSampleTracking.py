from LabSampleTracking import Sample,DNASample,RNASample
import unittest



class TestResults(unittest.TestCase):
    def setUp(self):
        self.sample = Sample(1,10.0,'collected')
        self.dna_sample = DNASample(1,45.2,2.4,'processing','human')
        self.rna_sample = RNASample(2,14.2,2.51,'collected',5.4)

    def test_sample_volume_sample(self):
        self.assertEqual(self.sample.volume,10.0)

    def test_sample_use_volume(self):
        self.sample.volume=1000
        prev_volume = self.sample.volume
        self.assertLess(self.sample.use_volume(5),prev_volume)

    def test_sample_update_status(self):
        current = self.sample.current_status
        self.assertNotEqual(current,self.sample.update_status("discarded"))
    def test_dna_is_human(self):
        self.assertEqual(self.dna_sample.type_dna,'human')

    def test_rna_is_degraded(self):
        self.assertTrue(self.rna_sample.integrity_score<5)

    def test_rna_integrity_score_valid(self):
        self.assertTrue(self.rna_sample._integrity_score,isinstance(self.rna_sample._integrity_score,float))

if __name__=='__main__':
    unittest.main()