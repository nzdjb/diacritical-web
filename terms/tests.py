from django.test import TestCase
from terms.models import Finding, Run, Term


class TermsTestCase(TestCase):
    def test_term_creation(self):
        Term.objects.create(term="Example Term")
        self.assertEqual(Term.objects.count(), 1)
        self.assertEqual(Term.objects.get(pk=1).term, "Example Term")

    def test_term_str(self):
        term = Term.objects.create(term="Example Term")
        self.assertEqual(str(term), "Example Term")

    def test_term_macron_support(self):
        term = Term.objects.create(term="Exámple Térm")
        self.assertEqual(str(term), "Exámple Térm")


class RunTestCase(TestCase):
    def setUp(self):
        self.term = Term.objects.create(term="Test Term")

    def test_run_creation(self):
        run = Run.objects.create(term=self.term)
        self.assertIsNotNone(run.pk)
        self.assertEqual(run.term, self.term)
        self.assertIsNotNone(run.start_time)
        self.assertEqual(len(run.secret), 32)
        self.assertTrue(run.secret.isalnum())

    def test_run_str(self):
        run = Run.objects.create(term=self.term)
        self.assertEqual(str(run), str(run.pk))


class FindingTestCase(TestCase):
    def setUp(self):
        term = Term.objects.create(term="Test Term")
        self.run_object = Run.objects.create(term=term)

    def test_finding_creation(self):
        finding = Finding.objects.create(
            run=self.run_object, url="http://example.com", page_name="Example Page"
        )
        self.assertIsNotNone(finding.pk)
        self.assertEqual(finding.run, self.run_object)
        self.assertEqual(finding.url, "http://example.com")
        self.assertEqual(finding.page_name, "Example Page")

        findings = Finding.objects.filter(run=self.run_object)
        self.assertEqual(findings.count(), 1)
        self.assertEqual(findings.first(), finding)

    def test_finding_str(self):
        finding = Finding.objects.create(
            run=self.run_object, url="http://example.com", page_name="Example Page"
        )
        self.assertEqual(str(finding), "Example Page")

    def test_multiple_findings(self):
        Finding.objects.create(
            run=self.run_object, url="http://example.com/1", page_name="Page 1"
        )
        Finding.objects.create(
            run=self.run_object, url="http://example.com/2", page_name="Page 2"
        )

        findings = Finding.objects.filter(run=self.run_object)
        self.assertEqual(findings.count(), 2)
        self.assertEqual(findings.get(pk=1).page_name, "Page 1")
        self.assertEqual(findings.get(pk=2).page_name, "Page 2")


class TermViewTestCase(TestCase):
    def setUp(self):
        self.term = Term.objects.create(term="Test Term")
        self.run_object = Run.objects.create(term=self.term)

    def test_term_view(self):
        response = self.client.get(f"/terms/{self.term.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Term")
        self.assertContains(response, str(self.run_object.pk))
