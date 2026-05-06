import React from 'react'
import Head from 'next/head'

export default function About(){
  return (
    <>
      <Head><title>About Us — Data Science Club</title></Head>

      <h1 className="text-4xl font-bold mb-2" style={{color: 'var(--primary)'}}>About Data Science Club</h1>
      <p className="text-lg text-slate-700 mb-12 pb-4 border-b-2" style={{borderBottomColor: 'rgba(0, 61, 153, 0.2)'}}>Empowering students and professionals through rigorous data scholarship</p>

      <section className="mb-12">
        <div className="flex items-center mb-4">
          <span className="inline-block w-2 h-2 rounded-full mr-3" style={{backgroundColor: 'var(--accent)'}}></span>
          <h2 className="text-2xl font-semibold" style={{color: 'var(--primary)'}}>Our Mission</h2>
        </div>
        <p className="text-slate-700 leading-relaxed bg-gradient-to-r from-blue-50 to-transparent p-6 rounded-lg border-l-4" style={{borderLeftColor: 'var(--accent)'}}>
          The Data Science Club is dedicated to advancing data literacy, rigorous analytical practice, and ethical use of data science across our institution and beyond. We foster a collaborative community of thinkers, analysts, and practitioners who engage with both theory and real-world applications.
        </p>
      </section>

      <section className="mb-12">
        <div className="flex items-center mb-4">
          <span className="inline-block w-2 h-2 rounded-full mr-3" style={{backgroundColor: 'var(--accent)'}}></span>
          <h2 className="text-2xl font-semibold" style={{color: 'var(--primary)'}}>Our Vision</h2>
        </div>
        <p className="text-slate-700 leading-relaxed bg-gradient-to-r from-blue-50 to-transparent p-6 rounded-lg border-l-4" style={{borderLeftColor: 'var(--accent)'}}>
          We envision a world where data science serves as a bridge between academic rigor and practical impact, where collaborative learning drives innovation, and where our community members emerge as leaders in their respective fields.
        </p>
      </section>

      <section className="mb-12">
        <div className="flex items-center mb-6">
          <span className="inline-block w-2 h-2 rounded-full mr-3" style={{backgroundColor: 'var(--accent)'}}></span>
          <h2 className="text-2xl font-semibold" style={{color: 'var(--primary)'}}>Core Values</h2>
        </div>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <h3 className="font-semibold mb-2 text-lg" style={{color: 'var(--primary)'}}>Rigor</h3>
            <p className="text-slate-700 text-sm leading-relaxed">Excellence in methodology, analytical thinking, and ethical standards in all our work.</p>
          </div>
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <h3 className="font-semibold mb-2 text-lg" style={{color: 'var(--primary)'}}>Collaboration</h3>
            <p className="text-slate-700 text-sm leading-relaxed">Working together across disciplines and industries to solve complex problems.</p>
          </div>
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <h3 className="font-semibold mb-2 text-lg" style={{color: 'var(--primary)'}}>Impact</h3>
            <p className="text-slate-700 text-sm leading-relaxed">Creating meaningful, real-world applications that drive positive change.</p>
          </div>
          <div className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <h3 className="font-semibold mb-2 text-lg" style={{color: 'var(--primary)'}}>Inclusivity</h3>
            <p className="text-slate-700 text-sm leading-relaxed">Building a welcoming community for learners at all stages and backgrounds.</p>
          </div>
        </div>
      </section>

      <section>
        <div className="flex items-center mb-4">
          <span className="inline-block w-2 h-2 rounded-full mr-3" style={{backgroundColor: 'var(--accent)'}}></span>
          <h2 className="text-2xl font-semibold" style={{color: 'var(--primary)'}}>Our History</h2>
        </div>
        <p className="text-slate-700 leading-relaxed mb-4 bg-gradient-to-r from-blue-50 to-transparent p-6 rounded-lg border-l-4" style={{borderLeftColor: 'var(--accent)'}}>
          Founded as a grassroots initiative, the Data Science Club has grown into a formal campus organization with strong partnerships across academia and industry. Over the years, we have hosted workshops, conferences, collaborative research projects, and mentorship programs that connect students with professionals.
        </p>
        <p className="text-slate-700 leading-relaxed bg-gradient-to-r from-blue-50 to-transparent p-6 rounded-lg border-l-4" style={{borderLeftColor: 'var(--accent)'}}>
          Today, we continue to expand our reach, building a network of practitioners and scholars committed to advancing the field of data science and its applications to real-world challenges.
        </p>
      </section>
    </>
  )
}
