from django.core.management.base import BaseCommand
from core.models import (
    BrandingSettings, Service, CoreValue, TeamMember, 
    Testimonial, FAQ, Partner, BlogPost, HeroSlide
)
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with professional sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Inaanza kuweka data... Tafadhali subiri...'))

        # 1. BRANDING SETTINGS (Rangi na Maandishi)
        branding, created = BrandingSettings.objects.get_or_create(id=1)
        branding.company_name = "Obrigado Finance"
        branding.primary_color = "#0f172a"  # Bluu ya Giza (Corporate)
        branding.secondary_color = "#10b981" # Kijani cha Emerald (Growth)
        branding.accent_color = "#f59e0b"    # Dhahabu (Wealth)
        branding.dark_color = "#020617"      # Nyeusi ya Top Bar/Footer
        branding.text_color = "#334155"      # Rangi ya maandishi
        branding.bg_color = "#f8fafc"        # Rangi nyepesi ya background
        branding.footer_text = "© 2026 Obrigado Finance. All rights reserved. Licensed financial institution."
        branding.whatsapp_number = "255700000000"
        
        branding.hero_title = "Welcome to Obrigado Finance"
        branding.hero_subtitle = "Your trusted partner for financial growth and stability."
        branding.hero_button_text = "Get Started"
        
        branding.about_title = "About Obrigado Finance"
        branding.about_subtitle = "Building financial bridges for a prosperous tomorrow."
        branding.about_mission = "To empower individuals and businesses with innovative financial solutions that drive growth, security, and long-term wealth. We believe that world-class financial services should be accessible, transparent, and tailored to your unique goals."
        branding.about_vision = "To be the global benchmark for financial excellence, offering a seamless digital experience and unparalleled expert guidance."
        
        branding.stat_1_value = "15+"
        branding.stat_1_label = "Years of Excellence"
        branding.stat_2_value = "1.2B+"
        branding.stat_2_label = "Assets Managed"
        branding.stat_3_value = "100k+"
        branding.stat_3_label = "Global Clients"
        
        branding.contact_address = "Obrigado Tower, 4th Floor\nPlot 123, Financial District\nDar es Salaam, Tanzania"
        branding.contact_email = "support@obrigadofinance.com"
        branding.contact_phone = "+255 700 123 456"
        branding.save()
        self.stdout.write(self.style.SUCCESS('[✓] Branding Settings zimewekwa'))

        # 2. HERO SLIDES
        HeroSlide.objects.all().delete()
        slides_data = [
            {
                'title': 'Empowering Your Financial Future',
                'subtitle': 'Experience world-class wealth management and investment strategies tailored for you.',
                'image': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop',
                'order': 1
            },
            {
                'title': 'Secure Investments. Higher Returns.',
                'subtitle': 'Grow your wealth with our highly secure and diversified global investment plans.',
                'image': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=2070&auto=format&fit=crop',
                'order': 2
            },
            {
                'title': 'Banking Without Borders',
                'subtitle': 'Send and receive money globally with lightning-fast speed and zero hidden fees.',
                'image': 'https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=2070&auto=format&fit=crop',
                'order': 3
            }
        ]
        for slide in slides_data:
            HeroSlide.objects.create(**slide)
        self.stdout.write(self.style.SUCCESS('[✓] Hero Slides zimewekwa'))

        # 3. SERVICES
        Service.objects.all().delete()
        services = [
            {"title": "Wealth Management", "description": "Personalized investment strategies designed to preserve and grow your wealth across global markets.", "icon": "📈"},
            {"title": "Corporate Banking", "description": "Comprehensive financial solutions for businesses of all sizes, from startups to multinational corporations.", "icon": "🏦"},
            {"title": "Smart Lending", "description": "Fast, flexible loan products with competitive rates, designed to fund your personal or business goals.", "icon": "💳"},
            {"title": "Global Transfers", "description": "Secure, lightning-fast international money transfers with real-time exchange rates and low fees.", "icon": "🌍"},
            {"title": "Retirement Planning", "description": "Ensure a comfortable and secure retirement with our tailored pension and savings plans.", "icon": "🌴"},
            {"title": "Digital Banking", "description": "Manage your finances on the go with our award-winning mobile banking application.", "icon": "📱"},
        ]
        for service in services:
            Service.objects.create(**service)
        self.stdout.write(self.style.SUCCESS('[✓] Services zimewekwa'))

        # 4. CORE VALUES
        CoreValue.objects.all().delete()
        values = [
            {"title": "Integrity", "description": "We uphold the highest ethical standards in every transaction and interaction.", "icon": "🛡️"},
            {"title": "Innovation", "description": "We leverage cutting-edge technology to provide seamless financial experiences.", "icon": "💡"},
            {"title": "Client First", "description": "Your success is our priority. We listen, adapt, and deliver.", "icon": "🤝"},
            {"title": "Excellence", "description": "We strive for perfection and consistently exceed expectations.", "icon": "🌟"},
        ]
        for value in values:
            CoreValue.objects.create(**value)
        self.stdout.write(self.style.SUCCESS('[✓] Core Values zimewekwa'))

        # 5. TEAM MEMBERS
        TeamMember.objects.all().delete()
        team = [
            {"name": "John M. Doe", "role": "Chief Executive Officer", "photo": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=300&auto=format&fit=crop", "bio": "With over 20 years in global finance, John leads the strategic vision of Obrigado."},
            {"name": "Sarah Jenkins", "role": "Chief Financial Officer", "photo": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=300&auto=format&fit=crop", "bio": "Sarah is an expert in corporate finance and wealth management strategies."},
            {"name": "David Osei", "role": "Head of Investments", "photo": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=300&auto=format&fit=crop", "bio": "David oversees our global investment portfolios and risk management."},
        ]
        for member in team:
            TeamMember.objects.create(**member)
        self.stdout.write(self.style.SUCCESS('[✓] Team Members zimewekwa'))

        # 6. TESTIMONIALS
        Testimonial.objects.all().delete()
        testimonials = [
            {"client_name": "Emily Clark", "company": "TechNova Inc.", "quote": "Obrigado Finance transformed how we manage our corporate assets. Their digital platform is unmatched.", "rating": 5},
            {"client_name": "Michael Chang", "company": "Global Logistics", "quote": "The global transfer services are lightning fast. We've saved thousands in transaction fees.", "rating": 5},
            {"client_name": "Amina Hassan", "company": "Hassan Enterprises", "quote": "Their wealth management team is truly professional. They helped me grow my portfolio by 30% in one year.", "rating": 5},
        ]
        for t in testimonials:
            Testimonial.objects.create(**t)
        self.stdout.write(self.style.SUCCESS('[✓] Testimonials zimewekwa'))

        # 7. FAQS
        FAQ.objects.all().delete()
        faqs = [
            {"question": "How do I open an account?", "answer": "You can open an account online by clicking the 'Get Started' button, or visit any of our branches with your ID and proof of address.", "order": 1},
            {"question": "What are the interest rates for loans?", "answer": "Our loan rates start from as low as 7.5% per annum, depending on your credit score, loan amount, and repayment period.", "order": 2},
            {"question": "Is my money safe with Obrigado Finance?", "answer": "Absolutely. We are a fully licensed financial institution. Your deposits are insured up to $250,000 per account.", "order": 3},
            {"question": "Do you offer international money transfers?", "answer": "Yes, we support transfers to over 150 countries with real-time exchange rates and low fees.", "order": 4},
        ]
        for faq in faqs:
            FAQ.objects.create(**faq)
        self.stdout.write(self.style.SUCCESS('[✓] FAQs zimewekwa'))

        # 8. PARTNERS
        Partner.objects.all().delete()
        partners = [
            {"name": "Visa"}, {"name": "Mastercard"}, {"name": "PayPal"}, 
            {"name": "Stripe"}, {"name": "CRDB Bank"}, {"name": "NMB Bank"},
        ]
        for p in partners:
            Partner.objects.create(**p)
        self.stdout.write(self.style.SUCCESS('[✓] Partners zimewekwa'))

        # 9. BLOG POSTS
        BlogPost.objects.all().delete()
        blogs = [
            {
                "title": "5 Smart Ways to Invest in 2026",
                "excerpt": "Discover the top investment strategies to maximize your wealth this year.",
                "content": "Investing in 2026 requires a blend of traditional stability and digital innovation. Here are 5 ways...\n\n1. Index Funds: ...\n2. Real Estate: ...\n3. Digital Assets: ...\n4. Corporate Bonds: ...\n5. Retirement Accounts: ...",
                "image": "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?q=80&w=800&auto=format&fit=crop",
            },
            {
                "title": "Understanding Global Market Trends",
                "excerpt": "A deep dive into the forces shaping the global economy and how to protect your portfolio.",
                "content": "The global economy is shifting. With inflation and changing interest rates, investors must be vigilant...\n\nIn this article, we explore the current trends in emerging markets and how Obrigado Finance can help you navigate them.",
                "image": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=800&auto=format&fit=crop",
            },
        ]
        for b in blogs:
            b['slug'] = slugify(b['title'])
            BlogPost.objects.create(**b)
        self.stdout.write(self.style.SUCCESS('[✓] Blog Posts zimewekwa'))

        self.stdout.write(self.style.SUCCESS('=== UMEMALIZA! Data zote za website zimewekwa kikamilifu. ==='))