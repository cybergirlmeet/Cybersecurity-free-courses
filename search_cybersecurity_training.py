import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

# Function to fetch and parse HTML content
def fetch_and_parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

# Function to extract links from HTML content
def extract_links(html_content, base_url):
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Convert relative links to absolute URLs
        absolute_url = urljoin(base_url, href)
        links.append(absolute_url)
    return links

# Main function to crawl web pages and find links based on topics
def crawl_and_scrape(topics_and_urls, max_pages=10):
    visited_urls = set()
    queue = deque([(url, 0, topic) for topic, urls in topics_and_urls.items() for url in urls])  # (url, depth, topic)

    while queue:
        url, depth, topic = queue.popleft()
        if url in visited_urls:
            continue
        visited_urls.add(url)
        
        print(f"Scraping {url} for topic: {topic}")
        html_content = fetch_and_parse(url)
        if not html_content:
            continue
        
        links = extract_links(html_content, url)
        relevant_links = [link for link in links if topic.lower() in link.lower()]  # Example filter
        
        # Print the found links
        for link in relevant_links:
            print(f"{topic}: {link}")
        
        # Add links to queue to follow related pages
        if depth + 1 <= max_pages:
            for link in links:
                queue.append((link, depth + 1, topic))

# Entry point of the script
if __name__ == "__main__":
    topics_and_urls = {
        'Free Cybersecurity Beginner Courses': [
            'https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/',
            'https://www.simplilearn.com/learn-cyber-security-basics-skillup',
            'https://www.mygreatlearning.com/cybersecurity/free-courses',
            'https://www.mygreatlearning.com/academy/learn-for-free/courses/introduction-to-cyber-security',
            'https://www.oxfordhomestudy.com/courses/cyber-security-courses/free-cyber-security-courses',
            'https://www.udemy.com/course/certified-secure-netizen/',
            'https://www.udemy.com/course/security-awareness-campaigns/',
            'https://www.udemy.com/tutorial/the-absolute-beginners-guide-to-information-cyber-security/the-trinity-of-it-security-cia/',
            'https://www.udemy.com/tutorial/comptia-security-plus-certification-prep/performing-vulnerability-assessments-part-1/',
            'https://www.udemy.com/tutorial/iso-27001-cybersecurity-manager-guidelines/cybersecurity/',
            'https://home.edx.org/',
            'https://www.simplilearn.com/free-cissp-training-skillup',
            'https://www.edx.org/learn/cybersecurity',
        ],
        'Free Cybersecurity Training Links': [
            'https://www.reddit.com/r/cybersecurity/comments/12670b4/for_anyone_looking_to_break_into_cybersecurity/',
            'https://www.fortinet.com/training/cybersecurity-professionals',
            'https://www.cisa.gov/cybersecurity-training-exercises',
            'https://www.sans.org/cyberaces/',
            'https://www.cybrary.it/',
            'https://niccs.cisa.gov/education-training/federal-virtual-training-environment-fedvte',
            'https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/',
            'https://www.isc2.org/landing/1mcc',
            'https://training.fortinet.com/',
            'https://niccs.cisa.gov/education-training',
        ],
        'Malware Analysis': [
            'https://lnkd.in/eSfp9jmv',
            'https://www.learn-c.org/',
            'https://lnkd.in/eCAygjEv',
            'https://lnkd.in/ewTd_dZu',
            'https://lnkd.in/eiQ3mGjY',
            'https://ow.ly/BxOy50NKB3U',
            'https://ow.ly/sBKw50NKB42',
            'https://ow.ly/sm4250NKB3P',
        ],
        'Reverse Engineering': [
            'https://lnkd.in/eUqUDdXS',
            'https://lnkd.in/ebtKjS-W',
            'https://beginners.re/',
            'https://lnkd.in/eUK3cdQc',
        ],
        'Web Pentesting Basics': [
            'https://buff.ly/3Uqh5o9',
            'https://buff.ly/3t103Pu',
        ],
        'Getting Started with Web Pentesting': [
            'https://buff.ly/3CdfFCt',
            'https://buff.ly/3UNpYcQ',
            'https://buff.ly/3Ux2rLI',
            'https://lnkd.in/gdhszwu2',
            'https://lnkd.in/gfnpNPpD',
            'https://lnkd.in/d2_6_-Qz',
            'https://buff.ly/3wlGHum',
        ],
        'Free Training and Resources': [
            'https://lnkd.in/gSZ8Jdpu',
            'https://lnkd.in/ghbx-baK',
            'https://lnkd.in/gpbnXmVH',
            'https://lnkd.in/g8RSjVpb',
            'https://lnkd.in/guW5SERh',
            'https://buff.ly/2Krir1d',
        ],
        'Specialised Training': [
            'https://lnkd.in/g64maMet',
            'https://lnkd.in/gXR5bD5N',
            'https://lnkd.in/g6cQjQuh',
            'https://lnkd.in/gs6Vn-DA',
            'https://lnkd.in/gnWVDCNp',
            'https://lnkd.in/g5SXKncJ',
            'https://lnkd.in/gZns6Xdf',
            'https://lnkd.in/gw22Y__E',
            'https://lnkd.in/gYAFfAuT',
            'https://lnkd.in/grrHivcW',
            'https://lnkd.in/gngVxhbu',
            'https://lnkd.in/gngVxhbu',
            'https://lnkd.in/gYNCGY8A',
            'https://lnkd.in/gYNCGY8A',
            'https://lnkd.in/ggpJ-vG6',
        ],
        'Incident Response': [
            'https://securityintelligence.com/articles/a-day-in-the-life-working-in-cyber-incident-response/',
            'https://learn.microsoft.com/en-us/security/incident-response/incident-response-overview',
            'https://csnp.org/courses/incident-response-process/',
            'https://dfirdiva.com/incident-response/free-incident-response-training-plan/',
            'https://dfir.training/',
            'https://www.hackthebox.com/blog/step-by-step-guide-to-writing-incident-response-reports',
            'https://www.itmasters.edu.au/incident-response-training/',
            'https://samsclass.info/152/',
            'https://www.netcomlearning.com/courses/cybersecurity-incident-management.html',
            'https://www.smartlearninguk.com/incident-management-training/',
            'https://www.isc2.org/training/online/incident-detection-and-response',
            'https://www.enisa.europa.eu/topics/trainings-for-cybersecurity-specialists/online-training-material',
            'https://www.bkminstitute.com/courses/cybersecurity-incident-management/',
        ],
        'API Security': [
            'https://api-fundamentals.example.com',
            'https://api-simplified.example.com',
            'https://api-methods.example.com',
            'https://api-terminologies.example.com',
            'https://api-authentication.example.com',
            'https://api-status-codes.example.com',
            'https://rest-api-vs-graphql.example.com',
            'https://api-integration.example.com',
            'https://api-integration-in-detail.example.com',
            'https://api-testing.example.com',
            'https://api-with-python.example.com',
            'https://api-scaling.example.com',
            'https://developing-robust-apis.example.com',
        ]
           
