import React from 'react'
import Head from 'next/head'
import Link from 'next/link'
import programs from '../data/initiatives'

export default function Initiatives(){
  return (
    <>
      <Head><title>Initiatives — Data Science Club</title></Head>

      <h1 className="text-4xl font-bold mb-2" style={{color: 'var(--primary)'}}>Our Initiatives</h1>
      <p className="text-lg text-slate-700 mb-12 pb-4 border-b-2" style={{borderBottomColor: 'rgba(0, 61, 153, 0.2)'}}>Advancing data science through education, research, and community engagement</p>

      <div className="grid md:grid-cols-2 gap-8">
        {programs.map((p, idx) => (
          <div key={p.slug} className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg group" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <div className="inline-block px-3 py-1 rounded-lg mb-3 font-bold text-sm" style={{backgroundColor: 'rgba(0, 61, 153, 0.1)', color: 'var(--accent)'}}>{String(idx + 1).padStart(2, '0')}</div>
            <h3 className="text-xl font-semibold mb-3" style={{color: 'var(--primary)'}}>{p.title}</h3>
            <p className="text-slate-700 leading-relaxed">{p.desc}</p>
            <Link href={`/initiatives/${p.slug}`} className="mt-4 inline-block text-sm font-medium transition-all duration-300 group-hover:translate-x-1" style={{color: 'var(--accent)'}}>
              Learn more →
            </Link>
          </div>
        ))}
      </div>
    </>
  )
}
