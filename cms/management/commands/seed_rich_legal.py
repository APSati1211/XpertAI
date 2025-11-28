from django.core.management.base import BaseCommand
from legal.models import LegalPage

class Command(BaseCommand):
    help = 'Seeds professional Terms of Service and Privacy Policy content'

    def handle(self, *args, **kwargs):
        self.stdout.write('🚀 Seeding Professional Legal Content...')

        # --- 1. PRIVACY POLICY CONTENT ---
        privacy_content = """
            <h2>1. Introduction</h2>
            <p>Welcome to <strong>XpertAI Global</strong> ("Company", "we", "our", "us"). We are committed to protecting your personal information and your right to privacy. If you have any questions or concerns about our policy, or our practices with regards to your personal information, please contact us at <a href="mailto:privacy@xpertai.global">privacy@xpertai.global</a>.</p>
            
            <h2>2. Information We Collect</h2>
            <p>We collect personal information that you voluntarily provide to us when expressing an interest in obtaining information about us or our products and services, when participating in activities on the Website or otherwise contacting us.</p>
            <ul>
                <li><strong>Personal Data:</strong> Name, email address, phone number, and company details.</li>
                <li><strong>Usage Data:</strong> IP address, browser type, operating system, and usage patterns.</li>
            </ul>

            <h2>3. How We Use Your Information</h2>
            <p>We use personal information collected via our website for a variety of business purposes described below:</p>
            <ul>
                <li>To provide and maintain our Service.</li>
                <li>To notify you about changes to our Service.</li>
                <li>To allow you to participate in interactive features when you choose to do so.</li>
                <li>To provide customer support and respond to inquiries.</li>
            </ul>

            <h2>4. Data Security</h2>
            <p>We implement appropriate technical and organizational security measures designed to protect the security of any personal information we process. However, please also remember that we cannot guarantee that the internet itself is 100% secure.</p>

            <h2>5. Your Privacy Rights</h2>
            <p>Depending on your location, you may have the following rights regarding your personal data:</p>
            <ul>
                <li>The right to access – You have the right to request copies of your personal data.</li>
                <li>The right to rectification – You have the right to request that we correct any information you believe is inaccurate.</li>
                <li>The right to erasure – You have the right to request that we erase your personal data, under certain conditions.</li>
            </ul>

            <h2>6. Updates to This Policy</h2>
            <p>We may update this privacy policy from time to time. The updated version will be indicated by an updated "Revised" date and the updated version will be effective as soon as it is accessible.</p>
        """

        # --- 2. TERMS OF SERVICE CONTENT ---
        terms_content = """
            <h2>1. Agreement to Terms</h2>
            <p>These Terms of Service constitute a legally binding agreement made between you, whether personally or on behalf of an entity ("you") and <strong>XpertAI Global</strong>, concerning your access to and use of the XpertAI website as well as any other media form, media channel, mobile website or mobile application related, linked, or otherwise connected thereto (collectively, the "Site").</p>

            <h2>2. Intellectual Property Rights</h2>
            <p>Unless otherwise indicated, the Site is our proprietary property and all source code, databases, functionality, software, website designs, audio, video, text, photographs, and graphics on the Site (collectively, the "Content") and the trademarks, service marks, and logos contained therein (the "Marks") are owned or controlled by us or licensed to us, and are protected by copyright and trademark laws.</p>

            <h2>3. User Representations</h2>
            <p>By using the Site, you represent and warrant that:</p>
            <ul>
                <li>All registration information you submit will be true, accurate, current, and complete.</li>
                <li>You will maintain the accuracy of such information and promptly update such registration information as necessary.</li>
                <li>You have the legal capacity and you agree to comply with these Terms of Service.</li>
                <li>You will not use the Site for any illegal or unauthorized purpose.</li>
            </ul>

            <h2>4. Prohibited Activities</h2>
            <p>You may not access or use the Site for any purpose other than that for which we make the Site available. The Site may not be used in connection with any commercial endeavors except those that are specifically endorsed or approved by us.</p>

            <h2>5. Limitation of Liability</h2>
            <p>In no event will we or our directors, employees, or agents be liable to you or any third party for any direct, indirect, consequential, exemplary, incidental, special, or punitive damages, including lost profit, lost revenue, loss of data, or other damages arising from your use of the site, even if we have been advised of the possibility of such damages.</p>

            <h2>6. Governing Law</h2>
            <p>These Terms shall be governed by and defined following the laws of India. XpertAI Global and yourself irrevocably consent that the courts of Mumbai shall have exclusive jurisdiction to resolve any dispute which may arise in connection with these terms.</p>

            <h2>7. Contact Us</h2>
            <p>In order to resolve a complaint regarding the Site or to receive further information regarding use of the Site, please contact us at:</p>
            <p><strong>XpertAI Global</strong><br>123 Corporate Avenue, Mumbai<br>Email: legal@xpertai.global</p>
        """

        # Update or Create Pages
        LegalPage.objects.update_or_create(
            slug="privacy-policy",
            defaults={"title": "Privacy Policy", "content": privacy_content}
        )
        self.stdout.write("   ✅ Updated: Privacy Policy")

        LegalPage.objects.update_or_create(
            slug="terms-and-conditions",
            defaults={"title": "Terms of Service", "content": terms_content}
        )
        self.stdout.write("   ✅ Updated: Terms of Service")

        self.stdout.write(self.style.SUCCESS('🎉 Legal Pages Populated with Professional Content!'))