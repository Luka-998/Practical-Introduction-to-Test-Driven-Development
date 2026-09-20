from LabSampleTracking import Sample,DNASample,RNASample
import unittest



class TestResults(unittest.TestCase):
    def setUp(self):
        self.sample = Sample(1,10.0,'collected')
        self.dna_sample = DNASample(1,45.2,2.4,'processing','human')
        self.rna_sample = RNASample(2,14.2,2.51,'collected',3.5)

    def test_sample_volume_sample(self):
        self.assertEqual(self.sample.volume,10.0)

    def test_sample_use_volume(self):
        self.sample.volume=1000
        prev_volume = self.sample.volume
        self.assertLess(self.sample.use_volume(5),prev_volume)

    def test_invalid_volume(self):
        self.assertRaises(ValueError,Sample,1,-2.0,'collected')

    def test_use_volume_exact_zero(self):
        self.sample.use_volume(10)
        self.assertEqual(self.sample.volume,0)

    def test_use_volume_below_zero_raises(self):
        self.assertRaises(ValueError,self.sample.use_volume,15)

    def test_sample_update_status_change(self):
        self.sample.update_status("discarded")
        self.assertEqual(self.sample.current_status, "discarded")

    def test_sample_update_status_invalid(self):
        self.sample.update_status("archived")
        self.assertRaises(ValueError,self.sample.update_status,'processing')

    def test_sample_update_status_same_status(self):
        self.assertEqual(self.sample.update_status('collected'),'collected')

    def test_sample_invalid_status_creation(self):

        self.assertRaises(ValueError,Sample,1,10.0,'test123')

    def test_dna_is_human(self):
        self.assertEqual(self.dna_sample.type_dna,'human')

    def test_rna_is_degraded(self):
        self.assertTrue(self.rna_sample.is_degraded())

    def test_rna_integrity_score_validation_range(self):
        invalid_scores = [-5.0,-1.0,12.0]
        for score in invalid_scores:
            with self.subTest(score=score):
                self.assertRaises(ValueError,setattr,self.rna_sample,'integrity_score',score)

    def test_rna_integrity_score_type(self):
        self.assertRaises(TypeError,setattr,self.rna_sample,'integrity_score',10)

    def test_dna_sample_subclass_sample(self):
        self.assertIsInstance(self.dna_sample,Sample)

    def test_rna_sample_subclass_sample(self):
        self.assertIsInstance(self.rna_sample,Sample)

    def test_dna_sample_update_volume(self):
        current_volume = self.dna_sample.volume
        self.assertLess(self.dna_sample.use_volume(10),current_volume)

    def test_dna_sample_same_status(self):
        self.assertEqual(self.dna_sample.current_status,'processing')

    def test_dna_sample_update_status(self):
        current = self.dna_sample.update_status('processing')
        self.assertNotEqual(current,self.dna_sample.update_status('collected'))
if __name__=='__main__':
    unittest.main(verbosity=2)