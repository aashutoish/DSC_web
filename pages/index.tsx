import React from 'react'
import Head from 'next/head'

export default function Home(){
  const notices = [
    'Workshop proposals open — May 12, 2026',
    'Guest lecture: Data Ethics in AI — May 20, 2026',
    'Research fellow applications ongoing'
  ]

  const events = [
    { date: 'May 15', title: 'Data Fundamentals Workshop', desc: 'Hands-on introduction to data collection and curation.' },
    { date: 'May 22', title: 'Industry Networking Event', desc: 'Connect with data science professionals from leading organizations.' },
    { date: 'June 5', title: 'Annual Data Science Conference', desc: 'Showcase of research projects and industry insights.' }
  ]

  const testimonials = [
    { name: 'Sarah Chen', year: 'Class of 2023', text: 'The club transformed how I approach data problems. Real mentorship, real impact.' },
    { name: 'Marcus Johnson', year: 'Class of 2024', text: 'From student to project lead—the Data Science Club gave me the platform to grow.' },
    { name: 'Aisha Patel', year: 'Class of 2022', text: 'The collaborative projects opened doors I never imagined in my career.' }
  ]

  return (
    <>
      <Head>
        <title>Data Science Club — Home</title>
      </Head>

      {/* Hero Section */}
      <section className="mb-20 pb-8">
        <div className="relative">
          <div style={{
            background: 'linear-gradient(135deg, rgba(10, 61, 98, 0.05) 0%, rgba(0, 61, 153, 0.03) 100%)',
            borderRadius: '12px',
            padding: '3rem 2rem',
            borderLeft: '4px solid var(--accent)'
          }}>
            <h1 className="text-5xl font-bold mb-3" style={{color: 'var(--primary)'}}>Data Science Club</h1>
            <p className="text-xl text-slate-700 font-light">Leading the way with rigorous data scholarship and real-world impact</p>
            <div className="mt-4 flex items-center space-x-2">
              <span className="inline-block w-2 h-2 rounded-full" style={{backgroundColor: 'var(--accent)'}}></span>
              <span className="text-sm text-slate-600">Empowering students and professionals</span>
            </div>
          </div>
        </div>
      </section>

      {/* About Section with 3 Pillars */}
      <section className="mb-20">
        <div className="flex items-center mb-8">
          <h2 className="text-3xl font-bold" style={{color: 'var(--primary)'}}>About Data Science Club</h2>
          <div className="ml-4 flex-1 h-px" style={{background: 'linear-gradient(90deg, var(--accent), transparent)'}}></div>
        </div>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <div className="inline-block p-2 rounded-lg mb-3 font-bold" style={{backgroundColor: 'rgba(0, 61, 153, 0.1)', color: 'var(--accent)'}}>01</div>
            <h3 className="text-xl font-semibold mb-3" style={{color: 'var(--primary)'}}>Academic Excellence</h3>
            <p className="text-slate-700 leading-relaxed">Fostering rigorous inquiry through structured learning, research projects, and mentorship from experts.</p>
          </div>
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <div className="inline-block p-2 rounded-lg mb-3 font-bold" style={{backgroundColor: 'rgba(0, 61, 153, 0.1)', color: 'var(--accent)'}}>02</div>
            <h3 className="text-xl font-semibold mb-3" style={{color: 'var(--primary)'}}>Collaboration & Networking</h3>
            <p className="text-slate-700 leading-relaxed">Building meaningful connections across campus and industry, forging partnerships that drive innovation.</p>
          </div>
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <div className="inline-block p-2 rounded-lg mb-3 font-bold" style={{backgroundColor: 'rgba(0, 61, 153, 0.1)', color: 'var(--accent)'}}>03</div>
            <h3 className="text-xl font-semibold mb-3" style={{color: 'var(--primary)'}}>Support & Resources</h3>
            <p className="text-slate-700 leading-relaxed">Comprehensive career guidance, professional networking, and access to industry experts and mentors.</p>
          </div>
        </div>
      </section>

      {/* Notices Section */}
      <section className="mb-20">
        <div className="flex items-center mb-8">
          <h2 className="text-3xl font-bold" style={{color: 'var(--primary)'}}>Latest Notices</h2>
          <div className="ml-4 flex-1 h-px" style={{background: 'linear-gradient(90deg, var(--accent), transparent)'}}></div>
        </div>
        <div className="border-l-4 p-6 bg-gradient-to-br from-yellow-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
          <ul className="space-y-3">
            {notices.map((n, idx) => (
              <li key={n} className="text-slate-700 flex items-start group">
                <span className="mr-3 font-bold inline-block w-6 h-6 rounded-full flex items-center justify-center text-white text-sm" style={{backgroundColor: 'var(--accent)', minWidth: '24px'}}>
                  {idx + 1}
                </span>
                <span className="pt-0.5">{n}</span>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* Events Section */}
      <section className="mb-20">
        <div className="flex items-center mb-8">
          <h2 className="text-3xl font-bold" style={{color: 'var(--primary)'}}>Upcoming Events</h2>
          <div className="ml-4 flex-1 h-px" style={{background: 'linear-gradient(90deg, var(--accent), transparent)'}}></div>
        </div>
        <div className="grid md:grid-cols-3 gap-6">
          {events.map((e, idx) => (
            <div key={e.title} className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg group" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
              <div className="text-sm font-semibold mb-3 inline-block px-3 py-1 rounded-full" style={{backgroundColor: 'rgba(0, 61, 153, 0.1)', color: 'var(--accent)'}}>
                {e.date}
              </div>
              <h3 className="text-lg font-semibold mt-3 mb-3" style={{color: 'var(--primary)'}}>{e.title}</h3>
              <p className="text-slate-700 text-sm leading-relaxed">{e.desc}</p>
              <div className="mt-4 inline-block text-sm font-medium" style={{color: 'var(--accent)'}}>
                Learn more →
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="mb-12">
        <div className="flex items-center mb-8">
          <h2 className="text-3xl font-bold" style={{color: 'var(--primary)'}}>Member Stories</h2>
          <div className="ml-4 flex-1 h-px" style={{background: 'linear-gradient(90deg, var(--accent), transparent)'}}></div>
        </div>
        <div className="grid md:grid-cols-3 gap-6">
          {testimonials.map((t) => (
            <div key={t.name} className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
              <div className="mb-4 text-lg" style={{color: 'var(--accent)'}}>★ ★ ★ ★ ★ (Featured)</div>
              <p className="text-slate-700 italic leading-relaxed mb-4">"{t.text}"</p>
              <div className="pt-4 border-t border-gray-200">
                <div className="font-semibold" style={{color: 'var(--primary)'}}>{t.name}</div>
                <div className="text-sm text-slate-600">{t.year}</div>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  )
}

